n=int(input())
for i in range(n):
 a,b,c=tuple(map(int,input().split()))
 k=2*(abs(a-b))
 d= c+abs(a-b) if c<=k/2 else c-(abs(a-b))
 
 if d in [a,b] or d>k or a>k or b>k or c>k:
     print(-1)
 else:
     print(d)
