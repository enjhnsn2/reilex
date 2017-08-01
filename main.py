from loader import *
from constraint import *
from graph import *

a = load_elf("tests/lab1A")
instrs_a = a.lift()# creates a generator, which can only be iterated over once

b = load_elf("tests/cap_bin")
instrs_b = b.lift()

c = load_elf("tests/moveebxeax")
instrs_c = c.lift()

d = load_elf("cap_bin2")
instrs_d = d.lift()

e = load_elf("tests/jmp_test")
instrs_e = e.lift()

#for ins in instrs_e:
#	print ins
#	for il_ins in ins.il_instructions:
#		print il_ins

cfg_a = gen_CFG(instrs_a)
for i in cfg_a:
	print i

"""
cfg_b = gen_CFG(instrs_b)
for i in cfg_b:
	print i

cfg_c = gen_CFG(instrs_c)
for i in cfg_c:
	print i

cfg_d = gen_CFG(instrs_d)
for i in cfg_d:
	print i

cfg_e = gen_CFG(instrs_e)
for i in cfg_e:
	print i
	print cfg_e[i]


"""

#new_state = state()
#new_state.execute(instrs_e)


#for reg in new_state.registers:
#	print new_state.registers[reg].size()
#	print reg , " = ", new_state.registers[reg]

#for reg in new_state.temp_registers:
#	print new_state.temp_registers[reg].size()
#	print reg , " = ", new_state.temp_registers[reg]


#of = new_state.registers["of"]
#ebp = new_state.registers["ebp"]
#new_state.solver.add(ebp == 0)
#print new_state.solver.check()
#print new_state.solver.model()
