"""Main function for reilex, will call various tools as I complete them """

from verify_patch import *

e = load_elf("tests/jmp_test")
instrs_e = e.lift()

for ins in instrs_e:
	print ins
	for il_ins in ins.il_instructions:
		print il_ins


def main():
	verify_patch("tests/jmp_test")


if __name__ == "__main__":
	main()

