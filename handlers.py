
#Array of function pointers to various instruction handlers
#indexed by definitions of instructions in reil/definitions


#r_ins stands for reil instruction
def handle_add(r_ins):
	print "add_handled"

def handle_and(r_ins):
	print "and_handled"

def handle_bisz(r_ins):
	print "bisz_handled"

def handle_div(r_ins):
	print "div_handled"

def handle_jcc(r_ins):
	print "jcc_handled"

def handle_ldm(r_ins):
	print "ldm_handled"

def handle_mod(r_ins):
	print "mod_handled"

def handle_mul(r_ins):
	print "mul_handled"

def handle_nop(r_ins):
	print "nop_handled"

def handle_or(r_ins):
	print "or_handled"

def handle_stm(r_ins):
	print "stm_handled"

def handle_str(r_ins):
	print "str_handled"

def handle_sub(r_ins):
	print "sub_handled"

def handle_undef(r_ins):
	print "undef_handled"

def handle_ukn(r_ins):
	print "ukn_handled"

def handle_xor(r_ins):
	print "xor_handled"

def handle_bisnz(r_ins):
	print "bisnz_handled"

def handle_equ(r_ins):
	print "equ_handled"

def handle_lshl(r_ins):
	print "lshl_handled"

def handle_lshr(r_ins):
	print "lshr_handled"

def handle_ashr(r_ins):
	print "ashr_handled"

def handle_sdiv(r_ins):
	print "sdiv_handled"

def handle_sex(r_ins):
	print "sex_handled"

def handle_sys(r_ins):
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
