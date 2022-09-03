t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    a1=a[::2]
    a2=a[1::2]
    
    if len(set(list(map(lambda x:x%2,a1))))==1 and len(set(list(map(lambda x:x%2,a2))))==1:
        print("YES")
    else:
        print("NO")
