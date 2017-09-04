"""
Module for constructing Control Flow Graphs (cfg) 
CFG are represented with a dictionary of start_address:block
Blocks here refer to basic blocks, i.e code sequence with no branches 
besides at the entry and exit.

Top Level Interface:
gen_CFG(instructions): returns dictionary of id:block
bin_to_cfg: return control flow graph of binary
"""
import reil.x86.translator as lift
from reil.definitions import *
from loader import *
class block:
    """
    Class to represent basic block.

    Attributes:
    ID = unique identifier, equivalent to start address of the basic block
    Left =  if predicate evaluates to false, go to left block
    Right = if predicate evaluates to true, go to right block
    instrs = list of il_ins that are used in this block
    """

    def __init__(self):
        """Default constructor for block class"""
        self.id = -1
        self.left = -1
        self.right = -1
        self.ins = []

    def is_leaf(self):
        """Simply returns true if block is leaf of cfg """
        if (self.left == -1) and (self.right == -1):
            return True
        else:
            return False

def gen_CFG(instructions):
    """
    Generates CFG for a set of REIL instructions.

    Output: dictionary of id:block where blocks are the basic blocks of this cfg
    """

    blocks = {}
    myBlock = block()
    myBlock.id = 0 #First block starts at offset 0
    for ins in instructions:
        if myBlock.id == -1: #When we have a new block, assign an id
            myBlock.id = ins.address
        myBlock.ins.append(ins)

        if ins.ends_basic_block: #We need to start a new block
            assert ins.il_instructions[-1].opcode == 5
            jcc_output = ins.il_instructions[-1].output
            #Assign right pointer
            if type(jcc_output) == RegisterOperand:
                myBlock.right = jcc_output.name
            elif type(jcc_output) == TemporaryOperand:
                myBlock.right = jcc_output.name
            elif type(jcc_output) == ImmediateOperand:
                myBlock.right = jcc_output.value
            #Assign left pointer
            myBlock.left = ins.address + ins.size
            #Add block to list
            blocks.update({myBlock.id:myBlock})
            myBlock = block()   

    blocks.update({myBlock.id:myBlock})
    return blocks


def bin_to_cfg(filename):
    """Top level function that takes file name and generates CFG """
    elf = load_elf(filename)
    lifted_instrs = elf.lift()
    cfg = gen_CFG(lifted_instrs)
    return cfg
