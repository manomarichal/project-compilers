int a;

float foo(int a)
{
    if (1)
    {
        return a*2;
    }
    // warning for uncertain return
}

int bar()
{
    int inner()
    {
        1+1; // error for missing return (should this be a warning?)
    }
    return 1.5; // warning for implicit conversion
    1+1; // warning for unused code
}

int main ()
{
    a = foo(5.0); // 2x warning: arg & return value (implicit conversions)
    return 0;
}