n=int(input())
for i in range(n):
    _t=input()
    s=list(map(int,input().split()))
    if s==sorted(s):
        print("NO")
    else:
        print("YES")
    
