t=int(input())
for i in range(t):
    s=input()
    l=[]
    while "a" in s or "b" in s:
    
        if "a" in s and s.index("a")==0 and "b" in s:
            b=s.index("b")
            l.append(b)
            s=s[b:]
        elif  "a" in s and s.index("a")==0:
            l.append(len(s))
            s=""
        elif s.index("b")==0 and "a" in s:
            a=s.index("a")
            l.append(a)
            s=s[a:]
        else:
            l.append(len(s))
            s=""

    l=list(filter(lambda x: x==1,l))
    

    if len(l)==0:
        print("YES")
    else:
        print("NO")
            
