"""
Module for constructing Control Flow Graphs (cfg) 
CFG are represented with a dictionary of start_address:block
Blocks here refer to basic blocks, i.e code sequence with no branches 
besides at the entry and exit.

Top Level Interface:
gen_CFG(instructions): returns dictionary of id:block
"""
import reil.x86.translator as lift

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
			myBlock.right = ins.il_instructions[-1].output.value #Deal with other jcc offsets
			myBlock.left = ins.address + ins.size
			blocks.update({myBlock.id:myBlock})
			myBlock = block()	

	blocks.update({myBlock.id:myBlock})
	return blocks

