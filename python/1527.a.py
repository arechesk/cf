for i in range(int(input())):
    x=int(input())
    x=(x>>(len(bin(x))-3)<<(len(bin(x))-3))-1
    print(x)
