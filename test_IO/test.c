#include <stdio.h>
int main()
{
    float a = 10 > 12; //0
    float b = 10 < 12; //1
    float c = 10 == 12; //0
    float d = 10 == 10; //1
    float e = 10 >= 11; // 0
    float f = 10 >= 10; // 1
    float g = 10 >= 9; // 1
    float h = 10 <= 9; // 0
    float i = 10 <= 10; // 1
    float j = 10 <= 11; // 1
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