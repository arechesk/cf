n=input()
s=list(map(int,input().split()))
s2=list(zip(s,range(1,len(s)+1)))
s2=sorted(s2)
s2=[str(k) for i,k in s2]
print(" ".join(s2))
