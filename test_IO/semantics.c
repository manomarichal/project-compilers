int a;

float foo(int a)
{
    if (int tmp=1) // declaration inside if condition
    {
        tmp = tmp*2;
        return a*2;
    }
    // WARNING for uncertain return
}

int main()
{
    a = foo(5.0); // 2x WARNING: arg & return value (implicit conversions)
    int num = 15;
    int* ptr = &num;
    printf(ptr[0]); // using a ptr as an array
    bar(); // WARNING: implicit declaration (would be error if not defined later)
    return 0;
}

int bar()
{
    for (int i=0; i<=10; ++i) // declaration inside for initializer
    {
        ++i;
    }
    int inner()
    {
        1+1; // ERROR for missing return (should this be a warning?)
    }
    return 1.5; // WARNING for implicit conversion
    1+1; // WARNING for unused code
}