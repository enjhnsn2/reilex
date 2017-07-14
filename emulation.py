from handlers import *
from riel.definitions import *

#instructions = stream of ins
#ins = assembly instruction
#r_ins = reil instruction



#Registers and memory are initialized during execution
#Ideally this will make register infrastructure the same 
#with different architectures
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


#Assumption: reg has been intialized in the state
#Input: prints current symbolic state of register
	def print_reg(self,reg):
		print_expression(registers[reg])

def print_expression(expr):
	if type(expr.op1) != expression and type(expr.op2) != expression:
		ins_handler[expr.operator]



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


#currently stateful
def AST_generate(state, instructions):
	for ins in instructions:
		for il_ins in ins.il_instructions:
			state.update_reg(reg,expr(il_ins.opcode, il_ins.input0, il_ins.input1))







def eager_engine(instructions):
	for ins in instructions:
		for il_ins in ins.il_instructions: 
			ins_handler[il_ins.opcode](il_ins)
			


#def lazy_engine(instructions):
