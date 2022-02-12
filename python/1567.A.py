n=int(input())
for i in range(n):
    t=int(input())
    s=input()
    x={"U":"D","D":"U"}
    tbl=s.maketrans(x)
    print(s.translate(tbl))
    
