n=int(input())
s=list(map(int,input().split()))

s=sorted(s)
d=[abs(i-j) for i,j in zip(s[:n:2],s[1::2])]
print(sum(d))
