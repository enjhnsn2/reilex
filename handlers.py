"""
Module that containts functions to handle all REIL instructions

Called by state.step() instruction
Functions are called through array of function pointers (ins_handler)
Full instruction definitions located in reil/definition

Each instruction takes a state and a REIL instruction and updates the state by 
symbollically executing the instruction
"""

from z3 import *




#Fetch ops -> equalize size -> compute result -> correct size -> update state

def equalize_size(a,b):
	""" 
	Sign extends the smaller of two bitvectors so they have equal length

	This is neccessary for certain bitvector operations
	Outputs tuple of modified bitvectors
	"""
	diff = a.size() - b.size()
	if diff > 0:
		return (a,SignExt(diff,b))
	elif diff < 0:
		return (SignExt(-diff,a),b)
	else:
		return (a,b)


def set_size_signed(BV, n):
	"""
	Set a BitVector BV to size n.
	Signed extension if extension is neccessary
	"""
	diff = BV.size() - n
	if diff > 0:
		return Extract(n-1, 0, BV)
	elif diff < 0:
		return SignExt(-diff,BV)
	else:
		return BV


def set_size_unsigned(BV, n):
	"""
	Set a BitVector BV to size n. 
	Unsigned extension if extension is neccessary
	"""
	diff = BV.size() - n
	if diff > 0:
		return Extract(n-1, 0, BV)
	elif diff < 0:
		return ZeroExt(-diff,BV)
	else:
		return BV



def handle_add(state, il_ins):
	"""
	Handles add instruction 
	result = in0 + in1

	Input: literal/register, literal/register
	Side Effects: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 + in1)
	state.update_state(il_ins.output, result)


def handle_and(state, il_ins):
	"""
	Handles and instruction
	result = in0 & in1


	Input: literal/register, literal/register
	Side Effect: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 & in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_bisz(state, il_ins):
	"""
	Handles bisz instruction
	result = in0 == 0


	Input: literal/register
	Side Effect: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	result = If(in0 == 0, BitVecVal(1, 1), BitVecVal(0, 1))
	state.update_state(il_ins.output, result)


def handle_bsh(state, il_ins):
	"""
	Handles bsh instruction
	if in1 > 0: result = in0 << in1
	if in0 < 0: result = in0 >> in1

	Input: literal/register, literal/register
	Side Effect: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	if in1 > 0:
		result = in0 << in1
	if in1 < 0:
		result = LShR(in0, in1)
	else:
		result = in0
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_div(state, il_ins):
	"""
	Handles div instruction.
	result = in0 / in1 (unsigned)

	Input: literal/register, literal/register
	Side Effect: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = UDiv(in0, in1)
	result = set_size_unsigned(result, il_ins.output.size)
	state.update_state(il_ins.output, result)



#Type specification: literal/register -> register/literal/offset
def handle_jcc(state, il_ins):
	"""
	Control flow modification is currently handles outside this function
	May be used in the future
	"""
	pass

def handle_ldm(state, il_ins):
	"""
	Handles ldm instruction
	result = in0(memory)

	Input: literal/register(memory)
	Side Effect: updates register with result
	"""
	in0 = state.fetch_op_mem(il_ins.input0)
	result = in0 
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_mod(state, il_ins):
	"""
	Handles mod instruction
	result = in0 % in1

	Input: literal/register, literal/register
	Side Effect: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 % in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_mul(state, il_ins):
	"""
	Handles mul instruction
	result = in0 * in1 (signed)

	Input: literal/register, literal/register
	Side Effects: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 * in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_nop(state, il_ins):
	""" Handles nop instruction"""
	pass

def handle_or(state, il_ins):
	""" 
	Handles or instruction
	result = in0 | in1

	Input: literal/register, literal/register
	Side Effect: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 | in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)

def handle_stm(state, il_ins):
	"""
	Handles stm instruction
	result(memory) = in0

	Input: literal/register
	Side Effect: updates memory at literal/register
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	result = in0
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_str(state, il_ins):
	"""
	Handles str instruction
	result = in0

	Input: literal/register
	Side Effect: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	result = in0
	result = set_size_unsigned(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_sub(state, il_ins):
	"""
	Handles sub instruction
	result = in0 - in1

	Input: literal/register, literal/register
	Side Effect: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 - in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


#Flags register as undefined
#Type specification: None -> Register 
def handle_undef(state, il_ins):
	pass

#Type specification: None 
def handle_ukn(state, il_ins):
	"""
	handles ukn instruction.
	Instruction shows up when translation library doesnt recognize asm isntruction
	"""
	pass


def handle_xor(state, il_ins):
	"""
	handles xor instruction
	result = in0 ^ in1

	Input: literal/register, literal/register
	Side effects: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 ^ in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_bisnz(state, il_ins):
	"""
	handles bisnz instruction
	result = in0 != 0

	Input: literal/register
	Side Effects: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	result = If(in0 != 0, BitVecVal(1, 1), BitVecVal(0, 1))
	state.update_state(il_ins.output, result)


def handle_equ(state, il_ins):
	"""
	handles equ instruction
	result = in0 == in1

	Input: literal/register, literal/register
	Side Effect: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = If(in0 == in1, BitVecVal(1, 1), BitVecVal(0, 1))
	state.update_state(il_ins.output, result)


def handle_lshl(state, il_ins):
	"""
	Handles lshl instruction
	result = in0 << in1

	Input: literal/register, literal/register
	Side Effect: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 << in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_lshr(state, il_ins):
	"""
	Handles lshr instruction
	result = in0 >> in1 (logical shift right)

	Input: literal/register, literal/register
	Side Effect: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = LShR(in0, in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_ashr(state, il_ins):
	"""
	Handles ashr instruction
	result = in0 >> in1 (arithmetic shift right)

	Input: literal/register, literal/register
	Side Effect: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 >> in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_sdiv(state, il_ins):
	"""
	Handles sdiv instruction
	result = in0 / in1 (signed)

	Input: literal/register, literal/register
	Side effect: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 / in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_sex(state, il_ins):
	"""
	Handle sex instruction
	result = in0 (signed)

	Input: literal/register
	Side Effect: updates register with result
	"""
	in0 = state.fetch_op_lit(il_ins.input0)
	result = in0
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_sys(state, il_ins):
	"""
	Handles sys instruction

	Unsure about how to handle this as of right now
	"""
	pass

#Table of function pointers to the handlers for each REIL instruction
ins_handler = [
	handle_add,
	handle_and,
	handle_bisz,
	handle_bsh,
	handle_div,
	handle_jcc,
	handle_ldm,
	handle_mod,
	handle_mul,
	handle_nop,
	handle_or,
	handle_stm,
	handle_str,
	handle_sub,
	handle_undef,
	handle_ukn,
	handle_xor,
	handle_bisnz,
	handle_equ,
	handle_lshl,
	handle_lshr,
	handle_ashr,
	handle_sdiv,
	handle_sex,
	handle_sys
	]
