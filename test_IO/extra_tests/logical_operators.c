#include <stdio.h>
int main()
{
    int a = !10;
    int b = !0;
    float c = !10.0;
    float d = !0.0;
    printf("%d; ", a);
    printf("%d; ", b);
    printf("%f; ", c);
    printf("%f; ", d);

    a = 2 && 0;
    b = 2 && 1;
    c = 2.0 && 0.0;
    d = 2.0 && 1.0;
    printf("%d; ", a);
    printf("%d; ", b);
    printf("%f; ", c);
    printf("%f; ", d);

    a = 2 || 0;
    b = 0 || 0;
    c = 2.0 || 0.0;
    d = 0.0 || 0.0;
    printf("%d; ", a);
    printf("%d; ", b);
    printf("%f; ", c);
    printf("%f; ", d);

}

//expected 0101011011
