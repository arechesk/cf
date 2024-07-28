int n = int.Parse(Console.ReadLine());
string[] s = Console.ReadLine().Split(' ');

int r = Array.ConvertAll(s, int.Parse).Sum();
if (r == 0)
{
    Console.WriteLine("EASY");
}
else {
    Console.WriteLine("HARD");
}
