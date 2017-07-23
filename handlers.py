from z3 import *
#Array of function pointers to various instruction handlers
#indexed by definitions of instructions in reil/definitions


#in0 and in1 are bitvectors
#returns bitvector corresponding to post operation state


#How to deal with immediate operands????

#TODO:--------------
#handle_sex, handle_sys, handle_jcc, make sure signed/unsigned works

#Zero extends the smaller of two bitvectors so they have equal length
#Returns tuple of two bitvectors

def equalize_size(a,b):
	if b is None:
		return (a,b)
	diff = a.size() - b.size()
	if diff > 0:
		return (a,ZeroExt(diff,b))
	if diff < 0:
		return (ZeroExt(-diff,a),b)






#Size = bits of output

#Type specification: literal/register, literal/register -> register
def handle_add(in0, in1):
	print "add_handled"
#	in0, in1 = equalize_size(in0,in1)
	return (in0 + in1)

#Type specification: literal/register, literal/register -> register
def handle_and(in0, in1):
	print "and_handled"
#	in0, in1 = equalize_size(in0,in1)
	return (in0 & in1)

#Type specification: #Type specification: literal/register -> register
def handle_bisz(in0, in1):
	print "bisz_handled"
	return in0 == 0

#TODO: implement
#We need a state split here
#Type specification: literal/register, literal/register -> register
def handle_bsh(in0, in1):
	print "bsh_handled"
	
	if in1 > 0:
		return in0 << in1
	if in1 < 0:
		return LShR(in0, in1)
	return in0

#Type specification: literal/register, literal/register -> register
def handle_div(in0, in1):
	print "div_handled"
	return UDiv(in0, in1)

#Type specification: literal/register -> register/literal/offset
def handle_jcc(in0, in1):
	print "jcc_handled"

#Type specification: literal/register -> register
def handle_ldm(in0, in1):
	print "ldm_handled"
	return in0

#Type specification: literal/register, literal/register -> register
def handle_mod(in0, in1):
	print "mod_handled"
	return (in0 % in1)

#Type specification: literal/register, literal/register -> register
def handle_mul(in0, in1):
	print "mul_handled"
	return (in0 * in1)

#Type specification: None
def handle_nop(in0, in1):
	print "nop_handled"

#Type specification: literal/register, literal/register -> register
def handle_or(in0, in1):
	print "or_handled"
	return in0 | in1

#Type specification: literal/register -> literal/register
def handle_stm(in0, in1):
	print "stm_handled"
	return in0

#Type specification: literal/register -> register
def handle_str(in0, in1):
	print "str_handled"
	return in0

#Type specification: literal/register, literal/register -> register
def handle_sub(in0, in1):
	print "sub_handled"
	return in0 - in1


#TODO: figure out some way to flag reigster as defined
#Flags register as undefined
#Type specification: None -> Register 
def handle_undef(in0, in1):
	print "undef_handled"
	return "UNDEF"

#Type specification: None 
def handle_ukn(in0, in1):
	print "ukn_handled"

#Type specification: literal/register, literal/register -> register
def handle_xor(in0, in1):
	print "xor_handled"
	return in0 ^ in1

#Type specification: literal/register -> register
def handle_bisnz(in0, in1):
	print "bisnz_handled"
	return in0 != in1

#Type specification: literal/register -> register
def handle_equ(in0, in1):
	print "equ_handled"
	return in0 == in1

#Type specification: literal/register, literal/register -> register
def handle_lshl(in0, in1):
	print "lshl_handled"
	return in0 << in1

#Type specification: literal/register, literal/register -> register
def handle_lshr(in0, in1):
	print "lshr_handled"
	return LShR(in0, in1)

#Type specification: literal/register, literal/register -> register
def handle_ashr(in0, in1):
	print "ashr_handled"
	return in0 >> in1

#Type specification: literal/register, literal/register -> register
def handle_sdiv(in0, in1):
	print "sdiv_handled"
	return in0 / in1

#Same as STR, except it is sign extended
#Type specification: literal/register -> register
def handle_sex(in0, in1):
	print "sex_handled"
	return in0 

#Type specification: ???????????
def handle_sys(in0, in1):
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
