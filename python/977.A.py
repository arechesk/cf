n,k= tuple(map(int, input().split()))
while k>0:
    if str(n)[-1]!="0":
        n-=1
    else:
        n=int(n/10)
    k-=1
print(int(n))
