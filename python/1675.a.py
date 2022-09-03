t=int(input())
for i in range(t):
    a,b,c,x,y=tuple(map(int,input().split()))
    a=  a-x if a<=x else 0
    b=  b-y if b<=y else 0
    if c>=-(a+b):
        print("YES")
    else:
        print("NO")
