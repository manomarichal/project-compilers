#include <stdio.h>
int main()
{
    int a = !10;
    int b = !0;
    float c = !0.1;
    float d = !0.0;
    printf("%d; ", a);
    printf("%d; ", b);
    printf("%f; ", c);
    printf("%f; ", d);

    a = 2 && 0;
    b = 2 && 1;
    c = 0.1 && 0.0;
    d = 0.1 && 1.0;
    printf("\n%d; ", a);
    printf("%d; ", b);
    printf("%f; ", c);
    printf("%f; ", d);

    a = 0 || 0;
    b = 2 || 0;
    c = 0.0 || 0.0;
    d = 0.1 || 0.0;
    printf("\n%d; ", a);
    printf("%d; ", b);
    printf("%f; ", c);
    printf("%f; ", d);

}

//expected
//0; 1; 0.0; 1.0;
//0; 1; 0.0; 1.0;
//0; 1; 0.0; 1.0;
