n,k=list(map(int,input().split()))
s=list(map(int,input().split()))
ans=int(len([i for i in s if 5-i>=k])/3)
print(ans)
