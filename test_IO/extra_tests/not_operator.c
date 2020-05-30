#include <stdio.h>


int main(){
    int a = !10;
    int b = !0;
    float c = !10.0;
    float d = !0.0;
    printf("%d; ", a);
    printf("%d; ", b);
    printf("%f; ", c);
    printf("%f; ", d);
	return 1;
}

// expected 0; 1; 0; 1;

