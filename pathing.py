"""
Module for verifying binary files
Currently enumerates all end states of binary file
Suffers from path explosion to a great extent, so
it would be wise to use this mostly for verifying small patches

Top-level interface: 
verify_patch(filename): prints summary of all end states and some overall summary data
"""

from loader import *
from execution import *
from graph import *
import copy
from helper import *

"""
def left_valid(state, block, pivot_flag, jcc_in):
    if pivot_flag == 1:
        return False
    if pivot_flag == 0:
        return True
    if pivot_flag == -1:
        return False

    if type(jcc_in) == RegisterOperand:
        pivot_expression = state.registers[pivot_flag]
    elif type(jcc_in) == TemporaryOperand:
        pivot_expression = state.temp_registers[pivot_flag]

    pivot_expression = simplify(pivot_expression)
    if pivot_expression == 0:
        return True
    if pivot_expression == 1:
        return  False
"""

def is_valid_path(state, block, path, pivot_flag, jcc_in):
    """Valid pivot flags := 0, 1 , register, temporaryRegister """

    if pivot_flag == 1:
        return path == block.right
    if pivot_flag == 0:
        return path == block.left
    if path == -1:
        return False

    if type(jcc_in) == RegisterOperand:
        pivot_expression = state.registers[pivot_flag]
    elif type(jcc_in) == TemporaryOperand:
        pivot_expression = state.temp_registers[pivot_flag]

    pivot_expression = simplify(pivot_expression)
    if pivot_expression == 0:
        return (path == block.left)
    if pivot_expression == 1:
        return (path == block.right)
    
    state.solver.add(pivot_expression == 1)
    
    print state.solver.check()
                
    s = Solver()
    s.add(pivot_expression == 0)
    print s.check()
            
    if not s.check():
        return (path == block.right)
    else: 
        return (path == block.left)



def recursive_execute(state, block, cfg, leaf_fn = None, leaf_args = None, enter_fn = None, enter_args = None):
        print "Block ID = ", block.id, block.left, block.right
        if block.is_leaf():
            if leaf_fn != None:
                leaf_fn(leaf_args)
#               end_states.append(state)
            return

        state.execute(block.ins)
        state_left = copy.deepcopy(state)
        state_right = copy.deepcopy(state)

        jcc_in = block.ins[-1].il_instructions[-1].input0#Return input operand of jcc
        pivot_flag = val(jcc_in)

        print pivot_flag

#Big block was here

        if is_valid_path(state_left, block, block.left, pivot_flag, jcc_in):
            recursive_execute(state_left, cfg[block.left], cfg, leaf_fn = leaf_fn, leaf_args = state_left)

        if is_valid_path(state_right, block, block.right, pivot_flag, jcc_in) and block.right != block.left:
            recursive_execute(state_right, cfg[block.right], cfg, leaf_fn = leaf_fn, leaf_args=state_right)




def enumerate_end_states(init_state, init_block, cfg):
    end_states = []
    recursive_execute(init_state, init_block, cfg, leaf_fn = end_states.append, leaf_args = state)
    return end_states




#TODO-----------------
#2. Fix
#3. make it better printable
#3.5 refactor round 2
#4. Comment
#5. Test more
#6. Final cleanup/make presentable

