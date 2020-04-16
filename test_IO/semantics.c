int a;

float foo(int a)
{
    return a*2;
}

int bar()
{
    int inner()
    {
        1+1; // error for missing return (should this be a warning)
    }
    return 1.5; // warning for implicit conversion
}

int main ()
{
    a = foo(5.0); // 2x warning: arg & return value (implicit conversions)
    return 0;
}