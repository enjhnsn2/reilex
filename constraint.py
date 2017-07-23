from handlers import *
from reil.definitions import *

#registers = dictionary of Z3 BitVecRef
#memory = dictionary of Z3 BitVecRef

#fetch state -> inputs to handlers

#dictionary from names to expressions
class state:
	def __init__(self):
		self.registers = {} 
		self.temp_registers = {} #Temporary registers used by REIL
		self.memory = {}
		self.post_condition = 0
		self.solver = Solver()

	#Reg is string of register name
	#expr is a bitvector
	def update_reg(self,reg, expr):
		if reg.name in self.registers:
			self.registers[reg.name] = expr
		else:
			self.registers.update({reg.name:expr})

	def update_temp(self,reg, expr):
		if reg.name in self.temp_registers:
			self.temp_registers[reg.name] = expr
		else:
			self.temp_registers.update({reg.name:expr})


	def update_mem(self,addr, expr):
		if str(addr.value) in self.memory:
			self.memory[str(addr.value)] = expr
		else:
			self.memory.update({str(addr.value):expr})


#Is there a better way to do it than isinstance???
	def update_state(self,output,expr):
		if type(output) == RegisterOperand:
#		if isinstance(output, RegisterOperand):
			self.update_reg(output, expr)
		elif type(output) == TemporaryOperand:
#		elif isinstance(output, TemporaryOperand):
			self.update_temp(output, expr)
		elif type(output) == ImmediateOperand:
#		elif isinstance(output, ImmediateOperand):
			self.update_mem(output, expr)
		else:
			print "Something in update_state went wrong"


	def fetch_reg(self, reg):
		if reg.name in self.registers:
			return self.registers[reg.name]
		else:
			return BitVec(reg.name,reg.size)

	def fetch_temp(self, reg):
		if reg.name in self.temp_registers:
			return self.temp_registers[reg.name]
		else:
			return BitVec(reg.name,reg.size)

	def fetch_mem(self, addr):
		if addr in self.memory:
			return self.memory[str(addr.value)]
		else:
			return BitVec(str(addr.value), addr.size)

	#Can take in immediate or other stuff
	#takes in an operand and returns the expression it represents in the current state
	#If it doesn't currently have a state, create a new bitvector
	#TODO: HOW TO TELL DIFFERENCE BETWEEN MEMORY AND IMMEDIATE

	def fetch_op(self, op):
		if type(op) == RegisterOperand:
#		if isinstance(op, RegisterOperand):
			return self.fetch_reg(op)
		elif type(op) == TemporaryOperand:
#		elif isinstance(op, TemporaryOperand):
			return self.fetch_temp(op)
		elif type(op) == ImmediateOperand:
#		elif isinstance(op, ImmediateOperand):
			return self.fetch_mem(op)
#		else:
#			print "Something in fetch_op went wrong"
		return 0

	#execute a single REIL instruction on the state
	def step(self, il_ins):
		input0 = il_ins.input0 
		input1 = il_ins.input1
		output = il_ins.output
		opcode = il_ins.opcode

		in0 = self.fetch_op(input0)
		in1 = self.fetch_op(input1)


		result = ins_handler[opcode](in0,in1) # returns expression formed by instruction
		self.update_state(output, result)


#return the post state after instructions have been executed
#instructions = generator of assembly instructions (not REIL)
	def execute(self, instructions):
		for ins in instructions:
			for il_ins in ins.il_instructions:
				self.step(il_ins)
				

