from handlers import *
from reil.definitions import *

#registers = dictionary of Z3 BitVecRef/BitVecVal
#temp_registers = dictionary of Z3 BitVecRef/BitVecVal
#memory = dictionary of Z3 BitVecRef/BitVecVal
#post_condition: currently unused
#Solver: allows for soliving by using z3, might be refactored to elsewhere

class state:
	def __init__(self):
		self.registers = {} 
		self.temp_registers = {} #Temporary registers used by REIL
		self.memory = {}
		self.post_condition = 0
		self.solver = Solver()

	#Reg is string of register name
	#expr is a bitvector
	#Update reg to be equal to expr
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


#output = 
#push expr to value specified by output operand
	def update_state(self,output,expr):
		if type(output) == RegisterOperand:
			self.update_reg(output, expr)
		elif type(output) == TemporaryOperand:
			self.update_temp(output, expr)
		elif type(output) == ImmediateOperand:
			self.update_mem(output, expr)
		else:
			print "Something in update_state went wrong"

#Returns register if it exists, else returns fresh BitVec
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

#Interpret immediate values as memory accesses
	def fetch_op_mem(self, op):
		if type(op) == RegisterOperand:
			return self.fetch_reg(op)
		elif type(op) == TemporaryOperand:
			return self.fetch_temp(op)
		elif type(op) == ImmediateOperand:
			return self.fetch_mem(op)
		return 0

#Interpret immediate values as literals
	def fetch_op_lit(self, op):
		if type(op) == RegisterOperand:
			return self.fetch_reg(op)
		elif type(op) == TemporaryOperand:
			return self.fetch_temp(op)
		elif type(op) == ImmediateOperand:
			return BitVecVal(op.value, op.size)
		return 0

#Symbolically execute a single step
	def step(self, il_ins):
		ins_handler[il_ins.opcode](self, il_ins)


	def exec_block(self, instructions):
		for ins in instructions:
			for il_ins in ins.il_instructions:
				self.step(il_ins)


#TODO: executes single basic block
	def execute(self, instructions):
		for ins in instructions:
			for il_ins in ins.il_instructions:
				self.step(il_ins)

#cfg = dictionary of basic blocks
"""
def execute_graph(init_state, cfg): 
	init_state.execute()
	execute(cfg[0])
	execute(left)
	execute(right)
"""








	
				

