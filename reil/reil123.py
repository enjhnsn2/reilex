from x86 import translator
#from translator import *
file = open('cap_bin', 'rb')
file.seek(0x40)
content = file.read(0xc)
translate(content,0)
print "WOW"