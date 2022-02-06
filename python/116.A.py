n=int(input())
ans=0
c=0
for i in range(n):
    a,b=tuple(map(int,input().split()))
    c=c-a+b
    ans=max(ans,c)
print(ans)
