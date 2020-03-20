int a = 1;
int b = 5;
int * p = &a;
*p = b;
int c = *p;
printf(c);