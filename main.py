from loader import *
from emulation import *



b = load_elf("tests/cap_bin")
instrs_b = b.lift()
a = load_elf("tests/lab1A")
instrs_a = a.lift()# creates a generator, which can only be iterated over once
#for i in instrs_b:
#	print i
c = load_elf("tests/moveebxeax")
instrs_c = c.lift()




new_state = state()
new_state = new_state.execute(instrs_b)

for reg in new_state.registers:
	print reg , " = ", new_state.registers[reg].to_string()
#	print reg.to_string()

