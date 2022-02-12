n=int(input())
for i in range(n):
    k=int(input())
    s=list(map(int,input().split()))
    ans=0
    while s!=sorted(s):
        for j in range(ans%2,len(s)-1,2):
            if s[j]>s[j+1]:
                s[j],s[j+1]=s[j+1],s[j]
        ans+=1
    print(ans)
