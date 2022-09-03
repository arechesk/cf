t=int(input())
for i in range(t):
    n=int(input())
    a=sorted(list(map(int,input().split())))
    k=False
    ans=0
    for j in range(n-2):
        if a[j]==a[j+1]==a[j+2]:
            k=True
            ans=a[j]
    if k:
        print(ans)
    else:
        print(-1)
