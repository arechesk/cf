for _ in range(int(input())):
    n=int(input())
    s=list(map(int,input().split()))
    l=len(set(s))
    if not n%2==l%2:
        l-=1
    print(l)
