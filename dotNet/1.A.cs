using System;
namespace cf
{
    public class A1
    {
        public static void Main(String[] args)
        {
            string[] s = Console.ReadLine().Split(' ');
            Int64 n = int.Parse(s[0]);
            Int64 m = int.Parse(s[1]);
            Int64 a=int.Parse(s[2]);
            Int64 r=n/a;
            Int64 k = m / a;
            if (n % a != 0)
            {
                r += 1;
            }
            if (m % a != 0) k += 1;

            Console.WriteLine(r*k);
            

        }
    }
}

