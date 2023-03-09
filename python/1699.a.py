for _ in range(int(input())):
    n=int(input())
    
    if n%2==0:
        print(f"0 0 {n>>1}")
    else:
        print("-1")
