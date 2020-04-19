#include <stdio.h>

int test()
{
    char a[5] = "Hello";
    a[2] = 'P';
    printf("%s!\n", a);
}
int main(){
    char a[5] = "Hello";
    a[2] = 'P';
    printf("%s!\n", a);
}