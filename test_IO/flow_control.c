int a = 0;
for (int b = 0; b<10; b++)
{
    a++;
    if (a==4)
        continue;
    if(a==4 || a==5)
        break;
}
if (a==0)
{
    printf('a');
}
else
{
    switch (a)
    {
        case 1:
            break;
        case 5:
            printf(a);
            break;
    }
}
