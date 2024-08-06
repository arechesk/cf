using System;
using System.Linq;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[] s = Console.ReadLine().Split().Select(int.Parse).ToArray();

        Array.Sort(s);
        int sum = 0;
        for (int i = 0; i < n / 2; i++)
        {
            sum += Math.Abs(s[2 * i] - s[2 * i + 1]);
        }
        
        Console.WriteLine(sum);
    }
}
