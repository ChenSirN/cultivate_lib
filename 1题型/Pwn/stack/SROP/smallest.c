// gcc -no-pie -o smallest smallest.c
void main(){
	__asm__("xor %rax,%rax\n\t"
					"movl $0x400,%edx\n\t"
					"mov %rsp,%rsi\n\t"
					"mov %rax,%rdi\n\t"
					"syscall\n\t"
					"ret\n\t"
	);
}