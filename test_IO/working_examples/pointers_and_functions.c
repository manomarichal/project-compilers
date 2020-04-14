int swap_ptrs_values(char* a, char* b)
{
    char temp = *b;
    *b = *a;
    *a = temp;
    return 0;
}

int swap_ptrs(char** a, char** b)
{
    char* temp = *b;
    *b = *a;
    *a = temp;
    return 0;
}

int power_of(char* a)
{
    *a = *a * *a;
    return 0;
}

int main()
{
    char a = 2;
    char b = 3;
    char c = 4;
    char d = 5;
    char e = 6;
    char * a_ptr = &a;
    char * b_ptr = &b;
    char * c_ptr = &c;
    char * d_ptr = &d;
    char * e_ptr = &e;

    power_of(&a);
    power_of(a_ptr);
    printf(a); // expectd 16

    swap_ptrs(&b_ptr, &c_ptr);
    char t0 = *b_ptr;
    char t1 = *c_ptr;
    printf(b); // expected 3
    printf(c); // expected 4
    printf(t0); // expected 4
    printf(t1); // expected 3

    swap_ptrs_values(d_ptr, e_ptr);
    printf(d); // expected 6
    printf(e); // expected 5

    return 0;
}