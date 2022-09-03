for i in range(int(input())):
    k=input()
    s=list(map(int,input().split()))
    from functools import reduce
    print( reduce(lambda x,y:x|y,s))
    
