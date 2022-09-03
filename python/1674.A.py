t=int(input())
for i in range(t):
    x,y=tuple(map(int,input().split()))
    if y%x==0:
        print(f"1 {int(y/x)}")
    else:
        print("0 0")
