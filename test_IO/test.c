#include <stdio.h>

// expected 80

int main(){
    int a = 1;
    float b = 1;
    printf("%d", ++a);
    printf("%d", ++b);

    int c = 1;
    float d = 1;
    printf("%d", c++);
    printf("%d", d++);

    int e = 1;
    float f = 1;
    printf("%d", --e);
    printf("%d", --f);

    int g = 1;
    float h = 1;
    printf("%d", g--);
    printf("%d", h--);

	return 1;
}
