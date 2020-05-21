#include <stdio.h>
int main()
{
    float f = 10.0/3.0;
    float * p = &f;
    *p = 5.0/2.0;
    printf("%d", f);
}