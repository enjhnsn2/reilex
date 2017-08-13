"""
Module for loading binary files
Currently only loades 32 and 64 bit elf files

Top Level Interface: 
Load_elf(filename): Returns populated ELF object
"""

#TODO: pretty printing
#TODO: write some documentation
#TODO: convert print functions to __str__()

import struct
import reil.x86.translator as lift

def btoi8(f):
	"""Converts 8 bytes of binary to integer """
	return struct.unpack("Q",f.read(8))[0]
def btoi4(f):
	"""Converts 4 bytes of binary to integer """
	return struct.unpack("I",f.read(4))[0]
def btoi2(f):
	"""Converts 2 bytes of binary to integer """
	return struct.unpack("H",f.read(2))[0]
def btoi1(f):
	"""Converts 1 byte of binary to integer """
	return struct.unpack("B",f.read(1))[0]


class f_header:
	"""Class for ELF file headers"""
	def load32(self,f):
		"""Loads file header for 32 bit elf files"""
		f.seek(0)
		self.ei_mag =   struct.unpack("ssss",f.read(4))
		self.ei_class = btoi1(f)
		self.ei_data = btoi1(f)	
		self.ei_version = btoi1(f)
		self.ei_osabi = btoi1(f)
		self.ei_abiversion = btoi1(f)
		self.ei_pad = f.read(7) 
		self.e_type = btoi2(f)
		self.e_machine = btoi2(f)
		self.e_version = btoi4(f)
		self.e_entry = btoi4(f)
		self.e_phoff = btoi4(f)
		self.e_shoff = btoi4(f)
		self.e_flags = btoi4(f)
		self.e_ehsize = btoi2(f)
		self.e_phentsize = btoi2(f)
		self.e_phnum = btoi2(f)
		self.e_shentsize = btoi2(f)
		self.e_shnum = btoi2(f)
		self.shstrndx = btoi2(f)


	def load64(self,f):
		"""Loads file header for 64 bit elf files"""
		f.seek(0)
		self.ei_mag =   struct.unpack("ssss",f.read(4))
		self.ei_class = btoi1(f)
		self.ei_data = btoi1(f)	
		self.ei_version = btoi1(f)
		self.ei_osabi = btoi1(f)
		self.ei_abiversion = btoi1(f)
		self.ei_pad = f.read(7) 
		self.e_type = btoi2(f)
		self.e_machine = btoi2(f)
		self.e_version = btoi4(f)
		self.e_entry = btoi8(f)
		self.e_phoff = btoi8(f)
		self.e_shoff = btoi8(f)
		self.e_flags = btoi4(f)
		self.e_ehsize = btoi2(f)
		self.e_phentsize = btoi2(f)
		self.e_phnum = btoi2(f)
		self.e_shentsize = btoi2(f)
		self.e_shnum = btoi2(f)
		self.shstrndx = btoi2(f)

	def print_h(self):
		"""Prints file header values """
		print "magic: ", self.ei_mag
		print "class: ",self.ei_class  
		print "data: ", self.ei_data 
		print "version: ", self.ei_version  
		print "os abi: ", self.ei_osabi 
		print "abi version: ", self.ei_abiversion  
		print "padding: ", self.ei_pad 
		print "type: ", self.e_type 
		print "machine: ", self.e_machine  
		print "version: ", self.e_version  
		print "entry: ", self.e_entry  
		print "phoff: ", self.e_phoff  
		print "shoff: ", self.e_shoff  
		print "flags: ", self.e_flags  
		print "ehsize: ", self.e_ehsize 
		print "phentsize: ", self.e_phentsize  
		print "phnum: ", self.e_phnum 
		print "shentsize: ", self.e_shentsize
		print "shnum: ", self.e_shnum
		print "shstrndx: ", self.shstrndx 


class p_header:
	"""
	Class for ELF program headers.
	There is 1 program header per segment in the ELF file.
	"""
	def load32(self,f,start):
		"""Load program header for 32 bit ELF file"""
		f.seek(start)
		self.p_type = btoi4(f) 
		self.p_offset = btoi4(f)
		self.p_vaddr = btoi4(f)
		self.p_paddr = btoi4(f)
		self.p_filesz = btoi4(f)
		self.p_memsz = btoi4(f)
		self.p_flags = btoi4(f)
		self.p_align = btoi4(f)

	def load64(self,f,start):
		"""Load program header for 32 bit ELF file"""
		f.seek(start)
		self.p_type = btoi4(f) 
		self.p_flags = btoi4(f)
		self.p_offset = btoi8(f)
		self.p_vaddr = btoi8(f)
		self.p_addr = btoi8(f)
		self.p_filesz = btoi8(f)
		self.p_memsz = btoi8(f)
		self.p_align = btoi8(f)

	def print_h(self):
		"""Prints program header values """
		print "p_type: ", self.p_type 
		print "p_offset: ", self.p_offset
		print "p_vaddr: ", self.p_vaddr
		print "p_addr: ", self.p_addr
		print "p_filesz: ", self.p_filesz
		print "p_memsz: ", self.p_memsz
		print "p_flags: ", self.p_flags
		print "p_align: ", self.p_align

class s_header:
	"""
	Class for ELF section headers.
	There is 1 section header per section in the ELF file.
	"""
	def load32(self,f,start):
		"""Load section header for 32 bit ELF file"""
		f.seek(start)
		self.sh_name = btoi4(f)
		self.sh_type = btoi4(f)
		self.sh_flags = btoi4(f)
		self.sh_addr = btoi4(f)
		self.sh_offset = btoi4(f)
		self.sh_size = btoi4(f)
		self.sh_link = btoi4(f)
		self.sh_info =btoi4(f)
		self.sh_addralign = btoi4(f)
		self.sh_entsize = btoi4(f)

	def load64(self,f,start):
		"""Load section header for 64 bit ELF file"""
		f.seek(start)
		self.sh_name = btoi4(f)
		self.sh_type = btoi4(f)
		self.sh_flags = btoi8(f)
		self.sh_addr = btoi8(f)
		self.sh_offset = btoi8(f)
		self.sh_size = btoi8(f)
		self.sh_link = btoi4(f)
		self.sh_info =btoi4(f)
		self.sh_addralign = btoi8(f)
		self.sh_entsize = btoi8(f)

	def print_h(self):
		"""Prints section header values """
		print "sh_name: ", self.sh_name 
		print "sh_type", self.sh_type 
		print "sh_flags: ", self.sh_flags 
		print "sh_addr: ", self.sh_addr 
		print "sh_offset: ", self.sh_offset 
		print "sh_size: ", self.sh_size 
		print "sh_link: ", self.sh_link 
		print "sh_info: ", self.sh_info
		print "sh_addralign: ", self.sh_addralign 
		print "sh_entsize: ", self.sh_entsize 


class elf:
	"""
	Class for for loading elf files
	
	Attributes:
	Filename:  file name of elf loaded
	f_head: File header
	p_headers: List of program headers
	s_headers: List of section headers

	"""
	def __init__(self,filename):
		"""Simple constructor"""
		self.filename = filename


	def load32(self):
		"""Populate all metadata for 32 bit ELF"""
		with open(self.filename, 'rb') as f:
			self.f_head = f_header()
			self.f_head.load32(f)
			self.p_headers = []
			self.s_headers = []
			#Load program headers
			for i in range(self.f_head.e_phnum):
				p_head = p_header()
				p_head.load32(f, self.f_head.e_phentsize * i + self.f_head.e_phoff)
				self.p_headers.append(p_head)

			#Load section headers
			for i in range(self.f_head.e_shnum):
				s_head = s_header()
				s_head.load32(f,self.f_head.e_shentsize * i + self.f_head.e_shoff)
				self.s_headers.append(s_head)
		self.text_start = self.get_text_start()
		self.text_size = self.get_text_size()

	def load64(self):
		"""Populate all metadata for 64 bit ELF"""
		with open(self.filename, 'rb') as f:
			self.f_head = f_header()
			self.f_head.load64(f)
			self.p_headers = []
			self.s_headers = []
			#Load program headers
			for i in range(self.f_head.e_phnum):
				p_head = p_header()
				p_head.load64(f, self.f_head.e_phentsize * i + self.f_head.e_phoff)
				self.p_headers.append(p_head)

			#Load section headers
			for i in range(self.f_head.e_shnum):
				s_head = s_header()
				s_head.load64(f,self.f_head.e_shentsize * i + self.f_head.e_shoff)
				self.s_headers.append(s_head)
		self.text_start = self.get_text_start()
		self.text_size = self.get_text_size()


	def get_class(self):
		"""
		Return class field of ELF.
		Class field is used to determine whether it is 32 or 64 bit.
		"""
		with open(self.filename, 'rb') as f:
			f.seek(4)
			return btoi1(f)


	def get_text_start(self):
		"""Returns offset of text section of ELF"""
		strtab_off = 0
		for i in self.s_headers:
			if i.sh_type == 3:
				with open(self.filename, "r") as f:
					f.seek(i.sh_offset + i.sh_name)
					if f.read(9) == '.shstrtab':
						strtab_off = i.sh_offset
				
		with open(self.filename,"r") as f:
			for i in self.s_headers:
				f.seek(strtab_off + i.sh_name)
				name = f.read(5)
				if name  == '.text':
					return i.sh_offset


	def get_text_size(self):
		"""Returns size of text segment"""
		strtab_off = 0
		for i in self.s_headers:
			if i.sh_type == 3:
				with open(self.filename, "r") as f:
					f.seek(i.sh_offset + i.sh_name)
					if f.read(9) == '.shstrtab':
						strtab_off = i.sh_offset
				
		with open(self.filename,"r") as f:
			for i in self.s_headers:
				f.seek(strtab_off + i.sh_name)
				name = f.read(5)
				if name  == '.text':
					return i.sh_size

	def lift(self):
		"""
		Lifts executable code to REIL
		Output: generator of REIL instructions
		"""
		with open(self.filename,"r") as f:
			f.seek(self.text_start)
			content = f.read(self.text_size)
			if self.get_class() == 1:
				return lift.translate(content,0)
			else:
				return lift.translate(content,0,x86_64 = True)
			


def load_elf(filename):
	"""
	Top level function for loading elf files
	Output: populated elf object
	"""
	my_elf = elf(filename)

	if my_elf.get_class() == 1:
		my_elf.load32()
		return my_elf

	if my_elf.get_class() == 2:
		my_elf.load64()
		return my_elf
	else:
		print "ELF failed to load"



