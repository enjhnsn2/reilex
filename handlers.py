from z3 import *
#Array of function pointers to various instruction handlers
#indexed by definitions of instructions in reil/definitions


#in0 and in1 are bitvectors
#returns bitvector corresponding to post operation state


#Fetch ops -> equalize size -> compute result -> correct size -> update state

#TODO:--------------
#handle_sex, handle_sys, handle_jcc

#Insert to debug handler
def debug_handler(il_ins):
	print il_ins
	print il_ins.input0
	print il_ins.input1
	print il_ins.output
	print il_ins.opcode



#Sign extends the smaller of two bitvectors so they have equal length
#Returns tuple of two bitvectors

def equalize_size(a,b):
	diff = a.size() - b.size()
	if diff > 0:
		return (a,SignExt(diff,b))
	elif diff < 0:
		return (SignExt(-diff,a),b)
	else:
		return (a,b)

#Set a BitVector to a particular size
#If it needs to be extended, do it in a signed fashion
def set_size_signed(BV, n):
	diff = BV.size() - n
	if diff > 0:
		return Extract(n-1, 0, BV)
	elif diff < 0:
		return SignExt(-diff,BV)
	else:
		return BV

#Set a BitVector to a particular size
#If it needs to be extended, do it in an unsigned fashion
def set_size_unsigned(BV, n):
	diff = BV.size() - n
	if diff > 0:
		return Extract(n-1, 0, BV)
	elif diff < 0:
		return ZeroExt(-diff,BV)
	else:
		return BV


#Size = bits of output

#Type specification: literal/register, literal/register -> register
def handle_add(state, il_ins):
	print "add_handled"
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 + in1)
	state.update_state(il_ins.output, result)



#Type specification: literal/register, literal/register -> register
def handle_and(state, il_ins):
	print "and_handled"
	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 & in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


#Type specification: #Type specification: literal/register -> register
def handle_bisz(state, il_ins):
	print "bisz_handled"
	in0 = state.fetch_op_lit(il_ins.input0)
	result = (in0 == 0)
	state.update_state(il_ins.output, result)


#TODO: implement
#We need a state split here
#Type specification: literal/register, literal/register -> register
def handle_bsh(state, il_ins):
	print "bsh_handled"

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




#Type specification: literal/register, literal/register -> register
def handle_div(state, il_ins):
	print "div_handled"
#	return UDiv(in0, in1)

	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = UDiv(in0, in1)
	result = set_size_unsigned(result, il_ins.output.size)
	state.update_state(il_ins.output, result)



#Type specification: literal/register -> register/literal/offset
def handle_jcc(state, il_ins):
	print "jcc_handled"

#Type specification: literal/register -> register
def handle_ldm(state, il_ins):
	print "ldm_handled"
#	return in0

	in0 = state.fetch_op_mem(il_ins.input0)
	result = in0 
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)

#Type specification: literal/register, literal/register -> register
def handle_mod(state, il_ins):
	print "mod_handled"
#	return (in0 % in1)

	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 % in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


#Type specification: literal/register, literal/register -> register
def handle_mul(state, il_ins):
	print "mul_handled"
#	return (in0 * in1)

	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 * in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


#Type specification: None
def handle_nop(state, il_ins):
	print "nop_handled"

#Type specification: literal/register, literal/register -> register
def handle_or(state, il_ins):
	print "or_handled"

	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 | in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


#TODO: needs to store to memory
#Type specification: literal/register -> literal/register
def handle_stm(state, il_ins):
	print "stm_handled"

	in0 = state.fetch_op_lit(il_ins.input0)
	result = in0
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


#Type specification: literal/register -> register
def handle_str(state, il_ins):
	print "str_handled"

	in0 = state.fetch_op_lit(il_ins.input0)
	result = in0
	result = set_size_unsigned(result, il_ins.output.size)
	state.update_state(il_ins.output, result)


#Type specification: literal/register, literal/register -> register
def handle_sub(state, il_ins):
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
	print "ukn_handled"

#Type specification: literal/register, literal/register -> register
def handle_xor(state, il_ins):
	print "xor_handled"

	in0 = state.fetch_op_lit(il_ins.input0)
	in1 = state.fetch_op_lit(il_ins.input1)
	in0, in1 = equalize_size(in0,in1)
	result = (in0 ^ in1)
	result = set_size_signed(result, il_ins.output.size)
	state.update_state(il_ins.output, result)

#Type specification: literal/register -> register
def handle_bisnz(state, il_ins):
	print "bisnz_handled"

	in0 = state.fetch_op_lit(il_ins.input0)
	result = (in0 != 0)
	state.update_state(il_ins.output, result)


#Type specification: literal/register, literal/register -> register
def handle_equ(state, il_ins):
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
