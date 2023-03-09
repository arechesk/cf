for _ in range(int(input())):
    n=input()
    a=list(map(int,input().split()))
    ans=0
    from functools import reduce
    for i in range(len(a)):
        if a[i]==reduce(lambda x,y: x^y,a[:i]+a[i+1:]):
            ans=a[i]
            break
    print(ans)
        
