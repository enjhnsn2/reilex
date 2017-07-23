from handlers import *
from reil.definitions import *

#registers = dictionary of Z3 BitVecRef
#memory = dictionary of Z3 BitVecRef

#fetch state -> inputs to handlers

#Possibly dictionary from object to expression?
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
		if reg in self.registers:
			self.registers[reg] = expr
		else:
			self.registers.update({reg:expr})

	def update_temp(self,reg, expr):
		if reg in self.temp_registers:
			self.temp_registers[reg] = expr
		else:
			self.temp_registers.update({reg:expr})


	def update_mem(self,addr, expr):
		if addr in self.memory:
			self.memory[addr] = expr
		else:
			self.memory.update({addr:expr})


#Is there a better way to do it than isinstance???
	def update_state(self,output,expr):
		if isinstance(output, RegisterOperand):
			self.update_reg(output.name, expr)
		elif isinstance(output, TemporaryOperand):
			self.update_temp(output.name, expr)
		elif isinstance(output, ImmediateOperand):
			self.update_mem(output.value, expr)
		else print "Something in update_state went wrong"


	def fetch_reg(self, reg):
		if reg in registers:
			return registers[reg]
		else:
			return BitVec(reg.name,reg.size)

	def fetch_reg(self, reg):
		if reg in registers:
			return temp_registers[reg]
		else:
			return BitVec(reg.name,reg.size)

	def fetch_reg(self, addr):
		return memory[addr]
		if addr in memory:
			return memory[addr]
		else:
			return BitVec(addr.value, addr.size)

	#takes in an operand and returns the expression it represents in the current state
	#If it doesn't currently have a state, create a new bitvector
	def fetch_op(self, op):
		if isinstance(output, RegisterOperand):
			return self.fetch_reg(output.name, RegisterOperand)
		elif isinstance(output, TemporaryOperand):
			return self.fetch_temp(output.name, TemporaryOperand)
		elif isinstance(output, ImmediateOperand):
			return self.fetch_mem(output.value, ImmediateOperand)
		else print "Something in fetch_op went wrong"
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
				step(il_ins)
				

