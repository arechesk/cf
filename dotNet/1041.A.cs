int n = int.Parse(Console.ReadLine());
int[] s = Array.ConvertAll(Console.ReadLine().Split(' '), int.Parse);
Console.WriteLine(s.Max() - s.Min() - n + 1);
