using System;

class Program
{
    static void Main()
    {
        int n = int.Parse(Console.ReadLine());
        int[] ar1 = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

        Console.WriteLine(Tanos(ar1));
    }

    static int Tanos(int[] ar)
    {
        int m = ar.Length;
        if (IsSorted(ar))
        {
            return m;
        }
        else
        {
            return Math.Max(Tanos(SubArray(ar, 0, m / 2)), Tanos(SubArray(ar, m / 2, m)));
        }
    }

    static bool IsSorted(int[] arr)
    {
        for (int i = 1; i < arr.Length; i++)
        {
            if (arr[i] < arr[i - 1])
                return false;
        }
        return true;
    }

    static int[] SubArray(int[] arr, int start, int end)
    {
        int length = end - start;
        int[] subArray = new int[length];
        Array.Copy(arr, start, subArray, 0, length);
        return subArray;
    }
}
