from handlers import *
from reil.definitions import *

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

#def print_expression(expr):
#	if type(expr.op1) != expression and type(expr.op2) != expression:
#		ins_handler[expr.operator]


def op_to_string(op):
	op_type = type(op)
	if op_type == registeroperand:
		return op.name
	elif op_type == immediateoperand:
		return str(op.value)
	elif op_type == temporaryoperand:
		return op.name
	elif op_type == offsetoperand:
		return str(op.offset)
	else:
		return ""

#Input: Expression
#Output: string representation of that string
def print_expression(expr):
	if expr is None:
		return ""
	if type(expr.op1) != expression:
		op1_string = op_to_string(expr.op1)
	else:
		op1_string = print_expression(expr.op1)

	if type(expr.op2) != expression:
		op2_string = op_to_string(expr.op2)
	else:
		op2_string = print_expression(expr.op2)

	return "(" + op1_string + " " + _opcode_to_string(expr.opcode) + " " + op2_string + ")"

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
	expr = expression()
	for ins in instructions:
		for il_ins in ins.il_instructions:
			state.update_reg(reg,expr(il_ins.opcode, il_ins.input0, il_ins.input1))








def eager_engine(instructions):
	for ins in instructions:
		for il_ins in ins.il_instructions: 
			ins_handler[il_ins.opcode](il_ins)
			



