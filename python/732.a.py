n,r=tuple(map(int,input().split()))
acc=n
counter=0
while not ((acc-r)%10==0 or acc%10==0):
    acc+=n
    counter+=1
print(counter+1)
