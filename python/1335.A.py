n=int(input())
for i in range(n):
    k=int(input())
    if k<=2:
        print(0)
    else:
        print(int((k-1)/2))
