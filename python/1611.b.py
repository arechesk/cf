for _ in range(int(input())):
    a,b=tuple(map(int,input().split()))
    x=int((a+b)/4)
    y=min(a,b)
    print(min(x,y))

