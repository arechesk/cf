n,m,a=tuple(map(int,input().split()))
r=int(n/a) if n%a==0 else int(n/a)+1
k=int(m/a) if m%a==0 else int(m/a)+1
print(r*k)
