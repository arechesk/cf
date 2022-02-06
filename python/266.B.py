n,k=tuple(map(int,input().split()))
s=input()
def tick(s):
    a=[]
    for i in range(len(s)-1)[::-1]:
        if s[i]=="B" and s[i+1]=="G" and not i in a :
            s=s[:i]+"G"+"B"+s[i+2:]
            a.append(i-1)
    return s
for i in range(k):
    s=tick(s)
print(s)
