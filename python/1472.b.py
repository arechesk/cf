t=int(input())
for i in range(t):
    n=int(input())
    s=list(map(int,input().split()))
    if sum(s)%2==1:
        print("NO")
    elif len(s)%2==0 or s.count(1)>=2:
        print("YES")
    else:
        print("NO")
