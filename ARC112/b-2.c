int main()
{
    long long int b, c, ret;
    scanf("%lld %lld", &b, &c);

    if (b > 0)
    {
        ret = 2;
        if (c / 2 >= b)
            ret += b * 2 - 1;
        else
            ret += c / 2 + (c - 1) / 2;
        ret += (c - 1) / 2 + (c - 2) / 2;
    }
    else if (b == 0)
        ret = 1 + c / 2 + (c - 1) / 2;
    else
        ret = 2 + c / 2 + (c - 1) / 2 + ((c - 1) / 2 >= b * -2 ? b * -2 - 1 : (c - 1) / 2);
    printf("%lld", ret);

}