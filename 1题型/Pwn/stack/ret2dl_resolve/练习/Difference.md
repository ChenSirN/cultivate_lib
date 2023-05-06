在x64中，两个结构体的定义如下：

```c
typedef uint64_t Elf64_Xword;  
typedef int64_t  Elf64_Sxword;  
typedef uint64_t Elf64_Addr;  
typedef uint32_t Elf64_Word;  

typedef struct  
{  
  Elf64_Addr    r_offset;        /* Address */  
  Elf64_Xword    r_info;            /* Relocation type and symbol index */  
  Elf64_Sxword    r_addend;        /* Addend */  
} Elf64_Rela;  

#define ELF64_R_SYM(i)            ((i) >> 32)  
#define ELF64_R_TYPE(i)            ((i) & 0xffffffff)  

typedef struct  
{  
  Elf64_Word    st_name;        /* Symbol name (string tbl index) */  
  unsigned char    st_info;        /* Symbol type and binding */  
  unsigned char st_other;        /* Symbol visibility */  
  Elf64_Section    st_shndx;        /* Section index */  
  Elf64_Addr    st_value;        /* Symbol value */  
  Elf64_Xword    st_size;        /* Symbol size */  
} Elf64_Sym;
```

ELF64_Rela 与 Elf64_Sym 实例的大小都为24byte（0x18）



64位下，`Elf64_Rel`是通过下面的方式找到的，所以选择的地址也需要对齐:

```c
Elf64_Rel *reloc = JMPREL + reloc_offset * 0x18
```

