for _ in range(int(input())):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if a==b==[0,0]:
        print(0)
    elif a==b==[1,1]:
        print(2)
    else:
        print(1)
