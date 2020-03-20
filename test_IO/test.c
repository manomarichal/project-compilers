int a = 1;
int b = 5;
int * p1 = &a;
int * * p2 = &p1;
int * * * p3 = &p2;
***p3 = b;

printf(a);
printf(b);

// expected output: 5, 5