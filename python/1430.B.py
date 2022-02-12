n=int(input())
for i in range(n):
    m,k=tuple(map(int,input().split()))
    s=sorted(list(map(int,input().split())))
    s[-1]=s[-1]+sum(s[-1-k:-1])
    print(s[-1])
    
