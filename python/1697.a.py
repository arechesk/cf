for _ in range(int(input())):
    n,m=tuple(map(int,input().split()))
    a=list(map(int,input().split()))
    a=sum(a)-m
    print(max(0,a))
