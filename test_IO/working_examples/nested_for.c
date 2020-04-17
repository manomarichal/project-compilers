int nested_for() // returns 6*8
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


int main()
{
    int res = nested_for();
    printf(res);    // expected 72
    return 0;
}

