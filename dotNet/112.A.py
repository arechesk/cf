using System;

class Program
{
    static void Main()
    {
        string a = Console.ReadLine().ToUpper();
        string b = Console.ReadLine().ToUpper();

        int res=String.Compare(a, b, StringComparison.Ordinal);
        if(res>0)
            Console.WriteLine("1");
        else if (res==0) Console.WriteLine("0");
        else Console.WriteLine("-1");
        
    }
}
