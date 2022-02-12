n=int(input())
def swap(a,b):
    if len(a)==1:
        a,b=[max(a[0],b[0])],[min(a[0],b[0])]
        return a,b
    a=sorted(a)
    b=sorted(b)
    if a[0]<=b[-1]:
        a,b=a[1:]+[b[-1]], b[:-1]+[a[0]]
    return a,b
for i in range(n):
    m,k=tuple(map(int,input().split()))
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    for j in range(k):
        a,b=swap(a,b)
    print(sum(a))
    
    
