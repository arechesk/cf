n=int(input())
s=list(map(int,input().split()))

c=0
ans=0
for i in s:
    if c+i<0:
        ans+=(c-i)
    else:
        c+=i
print(ans)
        
