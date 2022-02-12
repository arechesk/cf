n=int(input())
s=list(map(int,input().split()))
a1=len([i for i in s if i==1])
a2=len([i for i in s if i==2])
a3=len([i for i in s if i==3])
k=min(a1,a2,a3)
print(k)
s=sorted(zip(s,range(1,n+1)))
a1=[i[1] for i in s if i[0]==1][:k]
a2=[i[1] for i in s if i[0]==2][:k]
a3=[i[1] for i in s if i[0]==3][:k]
for i,j,k in zip(a1,a2,a3):
    print(f"{i} {j} {k}")
