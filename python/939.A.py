n=int(input())
s=list(map(int,input().split()))
f={i:k for i,k in zip(range(1,n+1),s)}
for i in range(1,n+1):
    if i==f[f[f[i]]]:
        print("YES")
        import sys
        sys.exit(0)
print("NO")
        
    
