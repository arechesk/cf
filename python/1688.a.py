for i in range(int(input())):
    x=int(input())
    y=x&-x
    while True:
        if x&y>0 and x^y>0:
            break
        else:
            y+=1
    print(y)
