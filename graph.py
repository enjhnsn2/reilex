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
	while 1:
		myBlock = block()
		for ins in instsructions:
			if myBlock.id == -1:
				myBlock.id = ins.address
			myBlock.ins.append(ins)
			if ends_basic_block(ins):
				break
		blocks.update(myBlock.id:myBlock)
	return blocks




"""
for ins in instrs_e:
	print ins.address
	for il_ins in ins.il_instructions:
		print il_ins
"""