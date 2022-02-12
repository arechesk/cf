n=int(input())
for i in range(n):
    k=input()
    s=sorted(list(map(int,input().split())))
    ans=min([i-k for i,k in zip(s[1:],s[:-1])])
    print(ans)
