// gcc -m64 -no-pie -fno-builtin -fstack-protector -z lazy test.c -o test
#include <unistd.h>
#include <stdio.h>
#include <string.h>
char s1[40];
char s2[40] = "flag{Here's the flag in server file}";
char s3[40]= "flag{Here's the flag in server file}";

void sub_400425(){
	int i;
	puts("I've delete your girlfriend's secret in the server and kept it in my bss.");
	printf("I'll show you right now! Please wait.");
	fflush(stdout);
	for(i=0;i<5;i++){
		sleep(1);
		putchar('.');
		fflush(stdout);
	}
	memset(s1, 0, 40);
	puts("\nOhhhhhhh! I must have done something wrong.");
}

int sub_4007E0(){
	int i;
	char name[10];
	puts("Hey bro, forgive me this time. Fortunately, I have a back-up copy.");
	puts("But before that, may I have your name first please? I...fogot =v=.");
	read(0, name, 0x150);
	puts("Did I read too long?");
	name[1] = '\0';
	printf("emmm...%s, Forget that, I'm calling write function now.\n", name);
	fflush(stdout);
	sleep(3);
	memset(s2, 0, 40);
	puts("Oh, I think I should run at once.");
	return 0;
}

int main(){
	strcpy(s1, "flag{Here's the flag on server file}");
	sub_400425();
	return sub_4007E0();
}