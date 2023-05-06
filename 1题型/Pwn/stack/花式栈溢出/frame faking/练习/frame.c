// gcc -m64 -no-pie -fno-builtin -fstack-protector -z lazy frame.c -o frame
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int vul(){
	char gift[] = "Z^\xc3";
	char s[0x50];
	int i;
	printf("Don't cry, I'll give you a gift:%p\n", &s);
	fflush(stdout);
	for(i=0;i<2;i++){
		memset(s, 0, 0x50);
		write(1, ">", 1);
		fflush(stdout);
		read(0, s, 0x70);
		printf("%s", s);
		fflush(stdout);
	}
	return 0;
}

int main(){
	return vul();
}
