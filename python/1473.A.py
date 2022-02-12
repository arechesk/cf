n=int(input())
for i in range(n):
    k,d=tuple(map(int,input().split()))
    s=sorted(list(map(int,input().split())))
    if s[0]<=d and s[-1]<=d:
        print("YES")
    elif sum(s[:2])<=d and d<s[-1]:
        print("YES")
    else:
        print("NO")
