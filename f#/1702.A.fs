open System

let t = int (Console.ReadLine())
for _ in 1 .. t do
    let s = Console.ReadLine()
    let n = bigint.Parse(s)
    let power = pown 10I (s.Length - 1)
    printfn "%A" (n - power)
