
int main()
{
    int a = 1;
    int b = a++;
    int c = a--;
    int d = --a;
    int e = ++a;
    printf(a);
    printf(b);
    printf(c);
    printf(d);
    printf(e);

    int temp1 = 0;
    int temp2 = 0;

    int n = 0;
    while (n++ < 5)
    {
        temp1++;
    }

    n = 0;
    while (++n < 5)
    {
        temp2++;
    }
    printf(temp1);
    printf(temp2);
    return 0;
}