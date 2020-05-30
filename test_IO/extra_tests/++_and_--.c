#include <stdio.h>

int main(){
    int a = 1;
    float b = 1;
    printf("%d; ", ++a);
    printf("%f; ", ++b);

    int c = 1;
    float d = 1;
    printf("%d; ", c++);
    printf("%f; ", d++);

    int e = 1;
    float f = 1;
    printf("%d; ", --e);
    printf("%f; ", --f);

    int g = 1;
    float h = 1;
    printf("%d; ", g--);
    printf("%f; ", h--);

	return 0;
}

// expected 2; 2.0; 1; 1.0; 0; 0.0; 1; 1.0;
