n=int(input())
s=[input() for i in range(n)]
ans=1
for i in range(1,n):
    if s[i]!=s[i-1]:
        ans+=1
print(ans)
