// gcc -m32 -fno-stack-protector -no-pie -fno-builtin -z execstack -z lazy test.c -o test
#include <stdio.h>

void sub_8048760(){
	__asm__("push %ebp\n\t"
		"movl %esp,%ebp\n\t"
		"subl $0x40,%esp\n\t"
		"and $0xFFFFFFF0,%eax\n\t"
		"jmp *%esp\n\t"
		"ret\n\t"
	);
}

int vul(){
	char s[5];
	fgets(s, 60, stdin);
	return 0;
}

int main(){
	return vul();
}