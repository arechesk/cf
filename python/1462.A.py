n=int(input())
for i in range(n):
    h=input()
    s=list(map(int,input().split()))
    r=[]
    for j in range(len(s)):
        if j%2==0:
            r.append(s[0])
            s=s[1:]
        else:
            r.append(s[-1])
            s=s[:-1]

    print(" ".join([str(i) for i in r]))
    
