n,m=tuple(map(int,input().split()))
for i in range(1,n+1):
    if i%2!=0:
        print("#"*m)
    else:
        if int(i/2)%2!=0:
            print("."*(m-1)+"#")
        else:
            print("#"+"."*(m-1))
