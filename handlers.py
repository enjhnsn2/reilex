from z3 import *
#Array of function pointers to various instruction handlers
#indexed by definitions of instructions in reil/definitions


#r_ins stands for reil instruction
def handle_add(input0, input1, output):
	print "add_handled"
	in0 = BitVec("in0", 32)#adjust size, Inherit bitvecs from state if possible
	in1 = BitVec("in1", 32)
	return (in0 + in1)

def handle_and(input0, input1, output):
	print "and_handled"

def handle_bisz(input0, input1, output):
	print "bisz_handled"

def handle_div(input0, input1, output):
	print "div_handled"

def handle_jcc(input0, input1, output):
	print "jcc_handled"

def handle_ldm(input0, input1, output):
	print "ldm_handled"

def handle_mod(input0, input1, output):
	print "mod_handled"

def handle_mul(input0, input1, output):
	print "mul_handled"

def handle_nop(input0, input1, input2):
	print "nop_handled"

def handle_or(input0, input1, input2):
	print "or_handled"

def handle_stm(input0, input1, input2):
	print "stm_handled"

def handle_str(input0, input1, input2):
	print "str_handled"

def handle_sub(input0, input1, input2):
	print "sub_handled"

def handle_undef(input0, input1, input2):
	print "undef_handled"

def handle_ukn(input0, input1, input2):
	print "ukn_handled"

def handle_xor(input0, input1, input2):
	print "xor_handled"

def handle_bisnz(input0, input, output):
	print "bisnz_handled"

def handle_equ(input0, input, output):
	print "equ_handled"

def handle_lshl(input0, input, output):
	print "lshl_handled"

def handle_lshr(input0, input, output):
	print "lshr_handled"

def handle_ashr(input0, input, output):
	print "ashr_handled"

def handle_sdiv(input0, input, output):
	print "sdiv_handled"

def handle_sex(input0, input, output):
	print "sex_handled"

def handle_sys(input0, input, output):
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
