#include <stdio.h>


int main()
{
int a = 1;
int b = 5;
int * p1 = &a;
int * * p2 = &p1;
int * * * p3 = &p2;
***p3 = b;

printf("%d; ", a);
printf("%d; ", b);
printf("%d; ", ***p3);

return a;
}

// expected 5; 5; 5;