"""Main function for reilex, will call various tools as I complete them """
import sys
import argparse
from pathing import *



def unused_code(filename):
    """
    Example application of Reilex
    Print off list of basic blocks that are never reachable
    It does this by symbollically all satisfiable paths and comparing
    reached blocks with the blocks in CFG.
    This is obviously extremely expensive, so would not work nearly as well on
    commercial software.
    """
    #Read in binary file, lift to REIL, and structure as CFG
    cfg = bin_to_cfg(filename)

    init_block = cfg[0]
    init_state = state()
    used_blocks = enumerate_all_blocks(init_state, init_block, cfg)
    unused_blocks = []

    for block in cfg:
        if block not in used_blocks:
            unused_blocks.append(block)

    for block in unused_blocks:
        print "Unused block ID = ", block



def verify_patch(filename):

    """ 
    Example application of Reilex
    Print off list of all possible end state
    It does this by symbollically all satisfiable paths and comparing.
    This is obviously extremely expensive, so would not work nearly as well on
    commercial software. It is actually useful if you are writing a small - moderately sized
    assembly program, like a patch.
    """

    #Read in binary file, lift to REIL, and structure as CFG
    cfg = bin_to_cfg(filename)
 
    #Declare initial state
    init_block = cfg[0]
    init_state = state()
 
    #Enumerate all possible end states   
    end_states = enumerate_end_states(init_state, init_block, cfg)   


    #print relevant information amout enumerated end states 
    for i in end_states:
        print "Condition: ", i.solver
        print "Register State: "
        for j in i.registers:
            print j, simplify(i.registers[j])
        print "-----------------------"

def version():
    """Print version """
    print "Version: 0.0"

def main():
"""Main function: reads command line and dispatches to functions"""
    parser = argparse.ArgumentParser(description='Symbolic Execution of REIL code')
    parser.add_argument('action', help = 'action to be performed')  
    parser.add_argument('filename', help = 'filename of binary you are analyzing')

    args = parser.parse_args()
    action = args.action
    filename = args.filename
    if action == 'p':
        verify_patch(filename)
    elif action == 'V' or action == 'version':
        version()
    elif action == 'u':
        unused_code(filename)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

