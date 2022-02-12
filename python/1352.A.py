n=int(input())
for i in range(n):
    l=[]
    k=int(input())
    for i in range(1,len(str(k))+1):
        if not k%10**i==0:
            l.append(k%10**i)
            k-=l[-1]
    print(len(l))
    print(" ".join([str(i) for i in l]))
