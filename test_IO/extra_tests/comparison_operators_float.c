#include <stdio.h>
int main()
{
    int a = 10.0 > 12.0; //0
    int b = 10.0 < 12.0; //1
    int c = 10.0 == 12.0; //0
    int d = 10.0 == 10.0; //1
    int e = 10.0 >= 11.0; // 0
    int f = 10.0 >= 10.0; // 1
    int g = 10.0 >= 9.0; // 1
    int h = 10.0 <= 9.0; // 0
    int i = 10.0 <= 10.0; // 1
    int j = 10.0 <= 11.0; // 1
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
