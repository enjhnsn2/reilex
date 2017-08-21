"""
Module for verifying binary files
Currently enumerates all end states of binary file
Suffers from path explosion to a great extent, so
it would be wise to use this mostly for verifying small patches

Top-level interface: 
verify_patch(filename): prints summary of all end states and some overall summary data
"""

from loader import *
from execution import *
from graph import *
import copy
from helper import *


def is_valid_path(state, block, path, pivot_flag, jcc_in):
	"""Valid pivot flags := 0, 1 , register, temporaryRegister """

	if pivot_flag == 1:
		return path == block.right
	if pivot_flag == 0:
		return path == block.left
	if path == -1:
		return False

	if type(jcc_in) == RegisterOperand:
		pivot_expression = state.registers[pivot_flag]
	elif type(jcc_in) == TemporaryOperand:
		pivot_expression = state.temp_registers[pivot_flag]

	if simplify(pivot_expression) == 0:
		return (path == block.left)
	if simplify(pivot_expression) == 1:
		return (path == block.right)
	state.solver.add(pivot_expression)
	print state.solver.check()
				
	s = Solver()
	s.add(Not(pivot_expression))
	print s.check()
			
	if not s.check():
		return (path == block.right)





#change end states to a generator
def verify_patch(filename):

	elf = load_elf(filename)
	lifted_instrs = elf.lift()
	cfg = gen_CFG(lifted_instrs)

	init_block = cfg[0]
	init_state = state()
	
	
	end_states = []

	for i in cfg:
		il_ins = cfg[i].ins[-1].il_instructions
		print i, cfg[i].left, cfg[i].right, il_ins


#Don't follow unsat paths
#Duplicate end_States
#Mark what conditions lead to what end state
#Mark as "enumerate all end states"
#Input: single state
#Output: list of recursive states
	def recursive_execute(state, block):
		print "Block ID = ", block.id, block.left, block.right
		if block.left == -1 and block.right == -1:
			end_states.append(state)
			return

		state.execute(block.ins)
		state_left = copy.deepcopy(state)
		state_right = copy.deepcopy(state)

		jcc_in = block.ins[-1].il_instructions[-1].input0
		pivot_flag = val(jcc_in)

		print pivot_flag



		if is_valid_path(state_left, block, block.left, pivot_flag, jcc_in):
			recursive_execute(state_left, cfg[block.left])

		if is_valid_path(state_right, block, block.right, pivot_flag, jcc_in) and block.right != block.left:
			recursive_execute(state_right, cfg[block.right])


	recursive_execute(init_state, init_block)

	for i in end_states:
		for j in i.registers:
			print j, simplify(i.registers[j])
		print "-----------------------"


