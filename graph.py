import reil.x86.translator as lift
#Generating cfg
#ID = unique identifier
#Left =  if predicate evaluates to false, go to left block
#Right = if predicate evaluates to true, go to right block
#instrs = list of il_ins that are used in this block
#ID = assigned from from jcc offset
class block:
	def __init__(self):
		self.id = -1
		self.left = 0
		self.right = 0
		self.ins = []


#Set done somehow
#Returns dictionary of id(start address of block) -> block
#instructions should be lifted already
#TODO: write second pass function to assign left and right pointers


def gen_CFG(instructions):
	blocks = {}
	myBlock = block()
	myBlock.id = 0
	for ins in instructions:
		if myBlock.id == -1: #When we have a new block, assign an id
			myBlock.id = ins.address
		myBlock.ins.append(ins)

		if ins.ends_basic_block: #We need to start a new block
			blocks.update({myBlock.id:myBlock})
			myBlock = block()	

	blocks.update({myBlock.id:myBlock})
	return blocks


#Final block is getting tossed due to my logic mistake
