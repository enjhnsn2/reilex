from handlers import *
from reil.definitions import *

#registers = dictionary of Z3 BitVecRef
#memory = dictionary of Z3 BitVecRef

def step(il_ins):
	input0 = il_ins.input0 
	input1 = il_ins.input1
	output = il_ins.output
	opcode = il_ins.opcode

	ins_handler[opcode](input0,input1,output)


class state:
	def __init__(self):
		self.registers = {} 
		self.memory = {}
		self.post_condition = 0
#return the post state after instructions have been executed
#instructions = generator of assembly instructions (not REIL)
	def execute(self, instructions):
		for ins in instructions:
			for il_ins in ins.il_instructions:
				step(il_ins)
				