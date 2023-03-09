for _ in range(int(input())):
    n=int(input())
    k=n//3
    r=n%3
    if r==0:
        print(f"{k} {k+1} {k-1}")
    elif r==1:
        print(f"{k} {k+2} {k-1}")
    else:
        print(f"{k+1} {k+2} {k-1}")
