using System;
using System.Linq;

class Program
{
    static void Main()
    {
        string s = Console.ReadLine();
        int ans = s.Count(i => i == '4' || i == '7'); // Считаем количество '4' и '7'
        
        // Проверяем, состоит ли ans только из '4' и '7'
        bool result = ans.ToString().All(i => i == '4' || i == '7');
        
        if (result)
        {
            Console.WriteLine("YES");
        }
        else
        {
            Console.WriteLine("NO");
        }
    }
}
