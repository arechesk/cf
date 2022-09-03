n=int(input())
for i in range(n):
    a,b,c=tuple(map(int,input().split()))
    print(f"{a+b+c} {b+c} {c}")
