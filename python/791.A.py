l,b=tuple(map(int,input().split()))
ans=1
while True:
    l*=3
    b*=2
    if l>b: break
    ans+=1

print(ans)
