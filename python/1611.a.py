for _ in range(int(input())):
    n=int(input())
    if n%2==0:
        print(0)
    elif int(str(n)[0])%2==0:
        print(1)
    elif 0 in list(map(lambda x: int(x)%2, list(str(n)))):
        print(2)
    else:
        print(-1)
    
    
