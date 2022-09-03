n=int(input())
for i in range(n):
    t=input()
    s=list(map(int,input().split()))
    a=[]
    for j in range(len(s)):
        
        if s[j]==(sum(s[:j]+s[j+1:])/(len(s)-1)):
            a.append(True)
    if len(a)>0:
        print("YES")
    else:
        print("NO")
    
