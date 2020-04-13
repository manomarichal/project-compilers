int power(int org)
{
    return org*org;
}

int double_of(int org)
{
    return org*2;
}

int double_of_power(int org)
{
    return power(org)*2;
}

int volume_of_cuboid(int a, int b, int c)
{
    return a*b*c;
}

int main()
{
    int org = 10;
    int r1 = power(org);
    int r2 = double_of(org);
    int r3 = double_of_power(org);
    int r4 = volume_of_cuboid(r1, r2, r3);
    printf(r1);
    printf(r2);
    printf(r3);
    printf(r4); // expected 400 000
    return 0;
}