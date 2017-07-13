from loader import *
from emulation import *



b = load_elf("tests/cap_bin")
print b.text_start
print b.text_size
il_b = b.lift()
#for i in il_b:
#	print i

eager_engine(il_b)

a = load_elf("tests/lab1A")
print a.text_start
print a.text_size
il_a = a.lift()
for i in il_a:
	print i


#a.f_head.print_h()
#c = b.lift(b.get_text_start_64(), b.get_text_size_64()) 


"""
file = open('tests/cap_bin', 'rb')
		file.seek(0x40) # Start of text section
		content = file.read(0xc) # size of text section
		x = abc.translate(content,10,x86_64 = True, use_rip = True)
		for i in x:
			print i.address, i.mnemonic, i.ends_basic_block, i.size
			for j in i.il_instructions:
			print j
"""