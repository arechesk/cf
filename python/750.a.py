n,k=tuple(map(int,input().split()))
l=[i*5 for i in range(1,n+1)]
acc=0
counter=0
for i in l:
    if (240-k)>=(acc+i):
        acc+=i
        counter+=1
print(counter)
