from functools import reduce
n=int(input())
for i in range(n):
    k=int(input())
    s=list(map(int,input().split()))
    print(reduce(lambda x,y: x&y,s))

    
