#include <stdio.h>


int main()
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
    int t2 = 0;
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
            t2 = t2 + 1;
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

    int t3 = 0;
    while (t3 < 20)
    {
        t3 = t3 + 1;
        if (t3 > 10)
        {
            break;
        }
    }
    int total = t + t2 + t3;
    printf("%d", total);
    return 0;
}

// expected 87