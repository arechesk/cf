for _ in range(int(input())):
    n,m,k=tuple(map(int,input().split()))
    a=sorted(input())
    b=sorted(input())
    res=""
    f=k
    c=0
    while not( len(a)==0 or len(b)==0):

        if f>0:
            if a[0]<b[0]:
                if c==1:
                    f-=1
                    res+=a.pop(0)
                else:
                    c=1
                    f=k-1
                    res+=a.pop(0)
            else:
                if c==1:
                    c=2
                    f=k-1
                    res+=b.pop(0)
                else:
                    f-=1
                    res+=b.pop(0)
        else:
            if c==1:
                c=2
                f=k-1
                res+=b.pop(0)
            else:
                c=1
                f=k-1
                res+=a.pop(0)
    print(res)
                    
    
