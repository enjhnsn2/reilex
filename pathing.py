"""
Module for determining pathing strategies

Top-level interface: 
is_valid_path: check if a path is satisfiable
recursive_execute: recursively execute over a control flow graph
"""

from loader import *
from execution import *
from graph import *
import copy
from helper import *


def is_valid_path(state, block, path, jcc_in):
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

    pivot_flag = val(jcc_in)

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
        return True





def enumerate_end_states_h(state, block, cfg, end_states):
    print block.id
    state.execute(block.ins)

    if block.is_leaf():
        end_states.append(state)

    state_left = copy.deepcopy(state)
    state_right = copy.deepcopy(state)

    jcc_in = block.ins[-1].il_instructions[-1].input0 #Return input operand of jcc

    if is_valid_path(state_left, block, block.left, jcc_in):
        enumerate_end_states_h(state_left, cfg[block.left], cfg, end_states)

    if is_valid_path(state_right, block, block.right, jcc_in) and block.right != block.left:
        enumerate_end_states_h(state_right, cfg[block.right], cfg, end_states)
    



def enumerate_end_states(init_state, init_block, cfg):
    """
    Returns a list of all reachable blocks from a particular block
    Inputs: 
    init_state: Initial state of execution, 
    init_block: block to start at
    cfg: CFG to execute over
    Outputs: list of blocks
    """
    end_states = []
    enumerate_end_states_h(init_state, init_block, cfg, end_states)
    return end_states

def enumerate_all_blocks_h(state, block, cfg, used_blocks):
    
    used_blocks.append(block.id)

    state.execute(block.ins)

    state_left = copy.deepcopy(state)
    state_right = copy.deepcopy(state)

    jcc_in = block.ins[-1].il_instructions[-1].input0 #Return input operand of jcc
    

    if is_valid_path(state_left, block, block.left, jcc_in):
        enumerate_all_blocks_h(state_left, cfg[block.left], cfg, used_blocks)

    if is_valid_path(state_right, block, block.right, jcc_in) and block.right != block.left:
        enumerate_all_blocks_h(state_right, cfg[block.right], cfg, used_blocks)


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
    enumerate_all_blocks_h(init_state, init_block, cfg, used_blocks)
    return used_blocks

