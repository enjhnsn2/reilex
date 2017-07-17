from handlers import *
from reil.definitions import *
from reil.definitions import _opcode_to_string
#instructions = stream of ins
#ins = assembly instruction
#r_ins = reil instruction



#Registers and memory are initialized during execution
#Ideally this will make register infrastructure the same 
#with different architectures
class state:
	def __init__(self):
		self.registers = {} 
		self.memory = {}
		self.pc = 0


#Currenly starts all registers/state etc at a fresh state
#Output: New state
#What if output isnt register???
#output can be immediate operand?
#TODO: remove is_instance
	def execute(self,instructions):
		new_state = state()
		for ins in instructions:
			for il_ins in ins.il_instructions:
				print il_ins
				if isinstance(il_ins.output, RegisterOperand) or isinstance(il_ins.output,TemporaryOperand):
					new_state.update_reg(il_ins.output.name, expression(il_ins.opcode, il_ins.input0, il_ins.input1))
		return new_state



#Input: register to add to state
#Adds a register to however I plan on mapping registers to symbolic registers in state class
		

#	def update_mem(self,addr,expr):


#Input: register to update, expr to update it to
#expr should be expr or immediate_operand
	def update_reg(self,reg,expr):
		if reg not in self.registers:
			self.registers.update({reg:expr})
			self.registers[reg] = expr
		else:
			self.registers[reg] = expr(expr.operator,registers[reg],expr)


#Assumption: reg has been intialized in the state
#Input: prints current symbolic state of register
#	def print_reg(self,reg):
#		print_expression(registers[reg])

#def print_expression(expr):
#	if type(expr.op1) != expression and type(expr.op2) != expression:
#		ins_handler[expr.operator]


def op_to_string(op):
	op_type = type(op)
	if op_type == RegisterOperand:
		return op.name
	elif op_type == ImmediateOperand:
		return str(op.value)
	elif op_type == TemporaryOperand:
		return op.name
	elif op_type == OffsetOperand:
		return str(op.offset)
	else:
		return ""



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


	#Output: string representation of expression
	def to_string(self):
		if self is None:
			return ""
		if type(self.op1) != expression:
			op1_string = op_to_string(self.op1)
		else:
			op1_string = print_expression(self.op1)

		if type(self.op2) != expression:
			op2_string = op_to_string(self.op2)
		else:
			op2_string = print_expression(self.op2)

		return "(" + op1_string + " " + _opcode_to_string(self.operator) + " " + op2_string + ")"


#Input: expressions to append, op to replace with expr
	def append(self, expr, op):
		self.op = expr




#currently stateful
#Input, stream of instructions
#Output: expression representing an AST
#def AST_generate(state, instructions):
#	expr = expression()
#	for ins in instructions:
#		for il_ins in ins.il_instructions:
#			state.update_reg(reg,expr(il_ins.opcode, il_ins.input0, il_ins.input1))
#			ast = ast.append(il_ins
#			if 







def eager_engine(instructions):
	for ins in instructions:
		for il_ins in ins.il_instructions: 
			ins_handler[il_ins.opcode](il_ins)
			



