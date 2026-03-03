int t = int.Parse(Console.ReadLine());
while (t-- > 0)
{
    string s = Console.ReadLine();
    int len = s.Length;

    long power = 1;
    for (int i = 1; i < len; i++)
        power *= 10;

    long n = long.Parse(s);
    long result = n - power;

    Console.WriteLine(result);
}
