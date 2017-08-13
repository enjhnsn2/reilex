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


#TODO: handle this with a closure
#Input: single state
#Output: list of recursive states
	def recursive_execute(state, block):
		print "called!"
		if block.left == -1 and block.right == -1:
			end_states.append(state)
			return

		state.execute(block.ins)
		state_left = copy.deepcopy(state)
		state_right = copy.deepcopy(state)

		if block.left != -1:
			recursive_execute(state_left, cfg[block.left])
		if block.right != -1:
			recursive_execute(state_right, cfg[block.right])


	recursive_execute(init_state, init_block)

	for i in end_states:
		print i.id
		