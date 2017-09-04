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


def is_valid_path(state, block, path, pivot_flag, jcc_in):
    """ 
    Determines whether a particular path is satisfiable from the current state
    Inputs:
    state: Current state
    block: Current Block
    path: Whether we are checking left path or right path
    pivot_flag: Conditions of zero flag being == 1 
    jcc_in: Place that we are potentially jumping to
    Outputs: True if path is satisfiable, false otherwise

    """

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
    
                
    s = Solver()
    s.add(pivot_expression == 0)
            
    if not s.check():
        return (path == block.right)
    else: 
        return (path == block.left)



def recursive_execute(state, block, cfg, leaf_fn = None, leaf_args = None, enter_fn = None, enter_args = None):
    """
    Function to recursively execute over a control flow graph
    Inputs:
    state: Current state
    block: Current block
    cfg: Cfg to execute over
    leaf_fn, leaf_args = leaf_fn(leaf_args) called whenever a leaf of the cfg is found
    enter_fn, enter_args = enter_fn(enter_args) called whenever a new block is found
    """
    #Note: leaf_fn and enter_fn are kind of hacky, will be fixed soon
        if enter_fn != None:
            enter_fn(enter_args)

        if block.is_leaf():
            if leaf_fn != None:
                leaf_fn(leaf_args)
            return

        state.execute(block.ins)
        state_left = copy.deepcopy(state)
        state_right = copy.deepcopy(state)

        jcc_in = block.ins[-1].il_instructions[-1].input0 #Return input operand of jcc
        pivot_flag = val(jcc_in)



        if is_valid_path(state_left, block, block.left, pivot_flag, jcc_in):
            recursive_execute(state_left, cfg[block.left], cfg, leaf_fn = leaf_fn, leaf_args = state_left, enter_fn = enter_fn, enter_args = block.left)

        if is_valid_path(state_right, block, block.right, pivot_flag, jcc_in) and block.right != block.left:
            recursive_execute(state_right, cfg[block.right], cfg, leaf_fn = leaf_fn, leaf_args=state_right, enter_fn = enter_fn, enter_args = block.right)


def enumerate_all_blocks(init_state, init_block, cfg):
    """
    Returns a list of all reachable blocks from a particular block
    Inputs: 
    init_state: Initial state of execution, 
    init_block: block to start at
    cfg: CFG to execute over
    Outputs: list of blocks
    """
    used_blocks = []
    recursive_execute(init_state, init_block, cfg, enter_fn = used_blocks.append, enter_args = init_block.id)
    return used_blocks

def enumerate_end_states(init_state, init_block, cfg):
    """
    Returns a list of all possible end states from a given start state and start block
    Inputs: 
    init_state: Initial state of execution
    init_block: block to start at
    cfg: CFG to execute over
    Outputs: list of end states
    """
    end_states = []
    recursive_execute(init_state, init_block, cfg, leaf_fn = end_states.append, leaf_args = state)
    return end_states




#TODO-----------------
#4. Comment
#5 Update top level interface
#6. Final cleanup/make presentable
#7. Finish wiki

