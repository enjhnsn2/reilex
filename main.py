from loader import *
from constraint import *



b = load_elf("tests/cap_bin")
instrs_b = b.lift()
a = load_elf("tests/lab1A")
instrs_a = a.lift()# creates a generator, which can only be iterated over once

c = load_elf("tests/moveebxeax")
instrs_c = c.lift()

d = load_elf("cap_bin2")
instrs_d = d.lift()

#for ins in instrs_a:
#	for il_ins in ins.il_instructions:
#		print il_ins

new_state = state()
new_state.execute(instrs_a)


for reg in new_state.registers:
#	print new_state.registers[reg].size()
	print reg , " = ", new_state.registers[reg]

for reg in new_state.temp_registers:
	print new_state.temp_registers[reg].size()
	print reg , " = ", new_state.temp_registers[reg]


of = new_state.registers["of"]
ebp = new_state.registers["ebp"]
new_state.solver.add(ebp == 0)
print new_state.solver.check()
#print new_state.solver.model()
