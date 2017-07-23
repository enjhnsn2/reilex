from loader import *
from constraint import *



b = load_elf("tests/cap_bin")
instrs_b = b.lift()
a = load_elf("tests/lab1A")
instrs_a = a.lift()# creates a generator, which can only be iterated over once
#for i in instrs_b:
#	print i
c = load_elf("tests/moveebxeax")
instrs_c = c.lift()

d = load_elf("cap_bin2")
instrs_d = d.lift()
#for ins in instrs_c:
#	for il_ins in ins.il_instructions:
#		print il_ins

new_state = state()
new_state.execute(instrs_d)


for reg in new_state.registers:
	print type(reg)
	print type(new_state.registers[reg])
	print reg , " = ", new_state.registers[reg]
#	print reg.to_string()
#rax = new_state.registers["rax"]
#new_state.solver.add(rax < 3)
#print new_state.solver.check()
#print new_state.solver.model()
