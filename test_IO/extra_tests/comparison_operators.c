#include <stdio.h>
int main()
{
    int a = 10 > 12; //0
    int b = 10 < 12; //1
    int c = 10 == 12; //0
    int d = 10 == 10; //1
    int e = 10 >= 11; // 0
    int f = 10 >= 10; // 1
    int g = 10 >= 9; // 1
    int h = 10 <= 9; // 0
    int i = 10 <= 10; // 1
    int j = 10 <= 11; // 1
    printf("%d", a);
    printf("%d", b);
    printf("%d", c);
    printf("%d", d);
    printf("%d", e);
    printf("%d", f);
    printf("%d", g);
    printf("%d", h);
    printf("%d", i);
    printf("%d", j);
}

//expected 0101011011
