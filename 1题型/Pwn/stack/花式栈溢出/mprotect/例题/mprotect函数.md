函数原型：
int mprotect(const void *start, size_t len, int prot);

mprotect()函数把自start开始的、长度为len的内存区的保护属性修改为prot指定的值  
prot可取的值为0-7,与linux文件权限相同  
0为无法访问，1为可执行，2为可写，4为可读  
需要指出的是，指定的内存区间必须包含整个内存页(4K)，区间开始的地址start必须是一个内存页的起始地址，并且区间长度len必须是页大小的整数倍，即start地址与len应该是0x1000的倍数  
例如mprotect(0x8048000, 0x2000, 7)的意思就是将0x8048000-0x804A000的空间权限设置为可读可写可执行

构造rop时，可以考虑先调用该函数将bss段设置为可读可写可执行，在其上写入shellcode后跳转执行