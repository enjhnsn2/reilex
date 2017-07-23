from z3 import *
#Array of function pointers to various instruction handlers
#indexed by definitions of instructions in reil/definitions

#Where do we initialize bit vectors?
#in0 and in1 are bitvectors
#return bitvector corresponding to post operation state
#how to deal when in1 is not used??????
#How to deal with immediate operands????


#TODO:--------------
#handle_sex, handle_sys, handle_jcc


def handle_add(in0, in1):
	print "add_handled"
	return (in0 + in1)

def handle_and(in0, in1):
	print "and_handled"
	return (in0 & in1)

def handle_bisz(in0, in1):
	print "bisz_handled"
	return in0 == 0

#Signed vs unsigned division?
def handle_div(in0, in1):
	print "div_handled"
	return (in0 / in1)

def handle_jcc(in0, in1):
	print "jcc_handled"

def handle_ldm(in0, in1):
	print "ldm_handled"
	return in0

def handle_mod(in0, in1):
	print "mod_handled"
	return (in0 % in1)

def handle_mul(in0, in1):
	print "mul_handled"
	return (in0 * in1)

def handle_nop(in0, in1):
	print "nop_handled"


def handle_or(in0, in1):
	print "or_handled"
	return in0 | in1

def handle_stm(in0, in1):
	print "stm_handled"
	return in0

def handle_str(in0, in1):
	print "str_handled"
	return in0

def handle_sub(in0, in1):
	print "sub_handled"
	return in0 - in1

def handle_undef(in0, in1):
	print "undef_handled"

def handle_ukn(in0, in1):
	print "ukn_handled"

def handle_xor(in0, in1):
	print "xor_handled"
	return in0 ^ in1

def handle_bisnz(in0, in1):
	print "bisnz_handled"
	return in0 != in1

def handle_equ(in0, in1):
	print "equ_handled"
	return in0 == in1


def handle_lshl(in0, in1):
	print "lshl_handled"
	return in0 << in1

def handle_lshr(in0, in1):
	print "lshr_handled"
	retyrb in0 >> in1

def handle_ashr(in0, in1):
	print "ashr_handled"
	return in0 >> in1

def handle_sdiv(in0, in1):
	print "sdiv_handled"
	return in0 / in1

def handle_sex(in0, in1):
	print "sex_handled"

def handle_sys(in0, in1):
	print "sys_handled"


ins_handler = [
	handle_add,
	handle_and,
	handle_bisz,
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
