// gcc -no-pie -fno-stack-protector -o bof_x64 bof_x64.c
#include <unistd.h>
#include <stdio.h>
#include <string.h>

void vuln()
{
    char buf[100];
    setbuf(stdin, buf);
    read(0, buf, 256);
}
int main()
{
    char buf[100] = "Welcome!\n";
    char gifts[] = "\x5e\xc3\x5a\xc3";

    setbuf(stdout, buf);
    write(1, buf, strlen(buf));
    vuln();
    return 0;
}