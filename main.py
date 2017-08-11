from verify_patch import *
"""
a = load_elf("tests/lab1A")
instrs_a = a.lift()# creates a generator, which can only be iterated over once

b = load_elf("tests/cap_bin")
instrs_b = b.lift()

c = load_elf("tests/moveebxeax")
instrs_c = c.lift()

d = load_elf("cap_bin2")
instrs_d = d.lift()

e = load_elf("tests/jmp_test")
instrs_e = e.lift()
"""
#for ins in instrs_e:
#	print ins
#	for il_ins in ins.il_instructions:
#		print il_ins
"""

cfg_a = gen_CFG(instrs_a)
for i in cfg_a:
	print i


cfg_b = gen_CFG(instrs_b)
for i in cfg_b:
	print i

cfg_c = gen_CFG(instrs_c)
for i in cfg_c:
	print i

cfg_d = gen_CFG(instrs_d)
for i in cfg_d:
	print i


cfg_e = gen_CFG(instrs_e)
for i in cfg_e:
	jmp = cfg_e[i].ins[-1].il_instructions[-1]
	print i, jmp, jmp.opcode == 5, cfg_e[i].left, cfg_e[i].right
"""



#new_state = state()
#new_state.execute(instrs_e)


#for reg in new_state.registers:
#	print new_state.registers[reg].size()
#	print reg , " = ", new_state.registers[reg]

#for reg in new_state.temp_registers:
#	print new_state.temp_registers[reg].size()
#	print reg , " = ", new_state.temp_registers[reg]


#of = new_state.registers["of"]
#ebp = new_state.registers["ebp"]
#new_state.solver.add(ebp == 0)
#print new_state.solver.check()
#print new_state.solver.model()


#change end states to a generator
"""
def verify_patch(filename):
	elf = load_elf(filename)
	lifted_instrs = elf.lift()
	cfg = gen_CFG(lifted_instrs)

	init_block = cfg[0]
	init_state = state()
	
	
	end_states = []


#TODO: handle this with a closure
#Input: single state
#Output: list of recursive states
	def recursive_execute(state, block):
		if block.left == -1 and block.right == -1:
			end_states.append(state)
			return

		state.execute(block.ins)
		state_left = copy.deepcopy(state)
		state_right = copy.deepcopy(state)

		if block.left != -1:
			recursive_execute(state_left, cfg[block.left])
		if block.right != -1:
			recursive_execute(state_right, cfg[block.right])


	recursive_execute(init_state, init_block)

	for i in end_states:
		print i.id

"""
"""
	leaves = []

	for block in cfg:
		if block.left == -1 and block.right == -1:
			leaves.append(block)
		else:


	for i in leaves:
"""
	#We need to access all leaves of cfg tree
	#How do we handle loops?



def main():
	verify_patch("tests/jmp_test")


if __name__ == "__main__":
	main()






