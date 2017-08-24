"""Main function for reilex, will call various tools as I complete them """
import sys
import argparse
from pathing import *

#def reach(state, addr, cfg):



def unused_code(filename):
	elf = load_elf(filename)
	lifted_instrs = elf.lift()
	cfg = gen_CFG(lifted_instrs)
	init_block = cfg[0]
	init_state = state()
	recursive_execute(init_state, init_block, cfg, leaf_fn = end_states.append, leaf_args = state)


#change end states to a generator
def verify_patch(filename):

    elf = load_elf(filename)
    lifted_instrs = elf.lift()
    cfg = gen_CFG(lifted_instrs)

    init_block = cfg[0]
    init_state = state()
    
    end_states = enumerate_end_states(init_state, init_block, cfg)   

#    for i in cfg:
#        il_ins = cfg[i].ins[-1].il_instructions
#        print i, cfg[i].left, cfg[i].right, il_ins


    for i in end_states:
        print "Condition: ", i.solver
        print "Register State: "
        for j in i.registers:
            print j, simplify(i.registers[j])
        print "-----------------------"

def version():
	print "Version: 0.0"

def main():
#	verify_patch("tests/jmp_test")
#	filename = sys.argv[1]
#	verify_patch (filename)
#	verify_patch("tests/jcc_test")

	parser = argparse.ArgumentParser(description='Symbolic Execution of REIL code')
	parser.add_argument('action', help = 'action to be performed')	
	parser.add_argument('filename', help = 'filename of binary you are analyzing')

	args = parser.parse_args()
	action = args.action
	filename = args.filename
	if action == 'p':
		verify_patch(filename)
	elif action == 'V' or 'version':
		version()
	elif action == 'u':
		unused_code(filename)
	else:
		parser.print_help()
#	args.action(args.filename)

if __name__ == "__main__":
	main()

