"""
This module is for misc functions that don't really fit elsewhere
Right now mostly for extending REIL translation library
"""
from reil.definitions import *


"""
Helper function to conveniently return value of operand
This is neccesarry because at this time I do not wish to rework
the entire REIL translation library
"""
def val(op):
	if type(op) == RegisterOperand:
		return op.name
	elif type(op) == TemporaryOperand:
		return op.name
	elif type(op) == ImmediateOperand:
		return op.value
	elif type(op) == OffSetOperand:
		return op.value