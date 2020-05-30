#include <stdio.h>
int test(int a, int b, int c, int d, int e, int f, int g, int h, int i, int j)
{
    return a + b + c + d + e + f + g + h + i + j;
}
int main(){
    printf("%d", test(1, 2 , 3, 4 ,5, 6, 7, 8, 9, 10));
}

// expected 2; 2.0; 1; 1.0; 0; 0.0; 1; 1.0;
