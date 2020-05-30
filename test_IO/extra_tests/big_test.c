#include <stdio.h>
int main()
{
    char a = 1.25;
    char b = 4;
    // a random comment
    char * p1 = &a;
    *p1 = 1 && ' ';
    char * * p2 = &p1;
    *p2 = &b;
    b = ' ' > 'X';
    int res = *p1;
    printf("%d; ", res);

    float test = ((10 + - 1) * 6) % 2 + 6 + + + + + 7 + (*p1) * -(**p2);
    printf("%f", test);

    return res;
}

// expected 0; 13
