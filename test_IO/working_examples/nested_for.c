int nested_for1()
{
    int t = 0;
    for (int b=0;b<10;b = b +1)
    {
        if (b < 2)
        {
            continue;
        }
        for (int c=0;c<10;c = c +1)
        {
            if (b < 3)
            {
                continue;
            }
            t = t + 1;
            if (c == 7)
            {
                break;
            }
        }
        if (b == 8)
        {
            break;
        }
    }
    return t;
}

int nested_for2()
{
    int t = 0;
    for (int b=0;b<10;b = b +1)
    {
        if (b < 3)
        {
            continue;
        }
        for (int c=0;c<10;c = c +1)
        {
            if (b < 4)
            {
                continue;
            }
            t = t + 1;
            if (c == 6)
            {
                break;
            }
        }
        if (b == 7)
        {
            break;
        }
    }
    return t;
}
int main()
{
    int res = nested_for1();
    int res2 = nested_for2();
    int total = res + res2;
    printf(total);    // expected 76
    return 0;
}