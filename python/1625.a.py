for _ in range(int(input())):
    s=input()
    l=list(map(int,input().split()))
    l2=list(map(lambda x: f"{x:>032b}",l))
    s=""
    for i in range(32):
        r=[j[i] for j in l2]
        if r.count("0")>r.count("1"):
            r=0
        else:
            r=1
        s+=str(r)
    print(int(s,2))
