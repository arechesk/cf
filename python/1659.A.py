t=int(input())
def f(n,r,b):
    k=r/(b+1)
    s=""
    while b>0:
        k=int(r/(b+1))
        for i in range(k):
            s+="R"
        s+="B"
        r-=k
        b-=1
    for i in range(r):
        s+="R"
    return s
for i in range(t):
    n,r,b=list(map(int,input().split()))
    print(f(n,r,b))
