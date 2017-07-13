from handlers import *
#Input: Instruction stream

#instructions = stream of ins
#ins = assembly instruction
#r_ins = reil instruction

#Experimental symbolic engine
#Will build lazy engine later as it's more complicated




class state:
	def __init__(self):
		registers ={} 
		memory = {}
		pc = 0

#Input: register to add to state
#Adds a register to however I plan on mapping registers to symbolic registers in state class
		

#	def update_mem(self,addr,expr):


#Input: register to update, expr to update it to
#expr should be expr or immediate_operand
	def update_reg(self,reg,expr):
		if reg not in self.registers:
			self.registers.update({reg:expr})
			registers[reg] = expr


"""
#Abstract syntax tree will be tree of these
#Op1 and Op2 can be:
Nonetype
registeroperand
immediateoperand
temporaryoperand
offsetoperand
"""
class expression:
	def __init__(self, operator, op1 = None, op2 = None):
		self.operator = operator
		self.op1 = op1
		self.op2 = op2



def AST_generate(state, instructions):
	for ins in il_instructions:
		for il_ins in ins.il_instructions:
			state.update_reg(reg, expr(il_ins.opcode, il_ins.input0, il_ins.input1))




def eager_engine(instructions):
	for ins in instructions:
		for il_ins in ins.il_instructions: 
			ins_handler[il_ins.opcode](il_ins)
			


#def lazy_engine(instructions):
