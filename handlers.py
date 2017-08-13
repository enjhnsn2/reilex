from z3 import *
#Array of function pointers to various instruction handlers
#indexed by definitions of instructions in reil/definitions
#Instruction definitions found in reil/definitions

#returns bitvector corresponding to post operation state


#Fetch ops -> equalize size -> compute result -> correct size -> update state

#TODO:--------------
#handle_sex, handle_sys, handle_jcc



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

	Inputs: literal/register, literal/register
	Side Effects: register
	"""
	print "add_handled"
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 + in1)
	state.update_state(il_ins.output, result)


def handle_and(state, il_ins):
	"""
	Handles and instruction

	Inputs: literal/register, literal/register
	Side Effect: register
	"""
	print "and_handled"
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 & in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_bisz(state, il_ins):
	"""
	Handles bisz instruction

	Inputs: literal/register
	Side Effect: register
	"""
	print "bisz_handled"
	in0 = state.fetch_op_lit(il_ins.input0)
	result = (in0 == 0)
	state.update_state(il_ins.output, result)


#TODO: We need a state split here
def handle_bsh(state, il_ins):
	"""
	Handles bsh instruction

	Inputs: literal/register, literal/register
	Side Effect: register
	"""
	print "bsh_handled "
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

	Inputs: literal/register, literal/register
	Side Effect: register
	"""
	print "div_handled"
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
	print "jcc_handled"


def handle_ldm(state, il_ins):
	"""
	Handles ldm instruction

	Inputs: literal/register, literal is interpreted as memory access
	Side Effect: register
	"""
	print "ldm_handled"
	in0 = state.fetch_op_mem(il_ins.input0)
	result = in0 
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_mod(state, il_ins):
	"""
	Handles mod instruction

	Inputs: literal/register, literal/register
	Side Effect: register
	"""
	print "mod_handled"
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 % in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_mul(state, il_ins):
	"""
	Handles mul instruction

	Inputs: literal/register, literal/register
	Side Effects: register
	"""
	print "mul_handled"
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 * in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_nop(state, il_ins):
	""" Handles nop instruction"""
	print "nop_handled"


def handle_or(state, il_ins):
	""" 
	Handles or instruction

	Inputs: literal/register, literal/register
	Side Effect: register
	"""
	print "or_handled"
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 | in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)

#TODO: reigster needs to store to memory at symbolic location
def handle_stm(state, il_ins):
	"""
	Handles stm instruction

	Inputs: literal/register
	Side Effect: literal/register
	"""
	print "stm_handled"
	in0 = state.fetch_op_lit(il_ins.input0)
	result = in0
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_str(state, il_ins):
	"""
	Handles str instruction

	Inputs: literal/register
	Side Effect: register
	"""
	print "str_handled"
	in0 = state.fetch_op_lit(il_ins.input0)
	result = in0
	result = set_size_unsigned(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_sub(state, il_ins):
	"""
	Handles sub instruction

	Inputs: literal/register, literal/register
	Side Effect: register
	"""
	print "sub_handled"
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 - in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


#TODO: figure out some way to flag reigster as defined
#Flags register as undefined
#Type specification: None -> Register 
def handle_undef(state, il_ins):
	print "undef_handled"

#Type specification: None 
def handle_ukn(state, il_ins):
	"""
	handles ukn instruction.
	Instruction shows up when translation library doesnt recognize asm isntruction
	"""
	print "ukn_handled"


def handle_xor(state, il_ins):
	"""
	handles xor instruction

	Inputs: literal/register, literal/register
	Side effects: register
	"""
	print "xor_handled"
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 ^ in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


def handle_bisnz(state, il_ins):
	"""
	handles bisnz instruction
	
	Inputs: literal/register
	Side Effects: register
	"""
	print "bisnz_handled"
	in0 = state.fetch_op_lit(il_ins.input0)
	print "in0 = ", in0
	result = (in0 != 0)
	state.update_state(il_ins.output, result)


#Type specification: literal/register, literal/register -> register
def handle_equ(state, il_ins):
	"""
	handles equ instruction

	Inputs:
	Side Effect: 
	"""
	print "equ_handled"
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 == in1)
	state.update_state(il_ins.output, result)

#Type specification: literal/register, literal/register -> register
def handle_lshl(state, il_ins):
	print "lshl_handled"

	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 << in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


#Type specification: literal/register, literal/register -> register
def handle_lshr(state, il_ins):
	print "lshr_handled"
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = LShR(in0, in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)

#Type specification: literal/register, literal/register -> register
def handle_ashr(state, il_ins):
	print "ashr_handled"

	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 >> in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)

#Type specification: literal/register, literal/register -> register
def handle_sdiv(state, il_ins):
	print "sdiv_handled"

	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 / in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


#Same as STR, except it is sign extended
#Type specification: literal/register -> register
def handle_sex(state, il_ins):
	print "sex_handled"

	in0 = state.fetch_op_lit(il_ins.input0)
	result = in0
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)

#Type specification: ???????????
def handle_sys(state, il_ins):
	print "sys_handled"


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
