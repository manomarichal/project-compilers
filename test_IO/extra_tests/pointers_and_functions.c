#include <stdio.h>

int swap_ptrs_values(int* a, int* b)
{
    int temp = *b;
    *b = *a;
    *a = temp;
    return 0;
}

int swap_ptrs(int** a, int** b)
{
    int* temp = *b;
    *b = *a;
    *a = temp;
    return 0;
}

int power_of(int* a)
{
    *a = *a * *a;
    return 0;
}

int main()
{
    int a = 2;
    int b = 3;
    int c = 4;
    int d = 5;
    int e = 6;
    int * a_ptr = &a;
    int * b_ptr = &b;
    int * c_ptr = &c;
    int * d_ptr = &d;
    int * e_ptr = &e;

    power_of(&a);
    power_of(a_ptr);
    printf("%d; ", a); // expected 16

    swap_ptrs(&b_ptr, &c_ptr);
    int t0 = *b_ptr;
    int t1 = *c_ptr;
    printf("%d; ", b); // expected 3
    printf("%d; ", c); // expected 4
    printf("%d; ", t0); // expected 4
    printf("%d; ", t1); // expected 3

    swap_ptrs_values(d_ptr, e_ptr);
    printf("%d; ", d); // expected 6
    printf("%d; ", e); // expected 5

    return 0;
}
// expected 16; 3; 4; 4; 3; 6; 5;
