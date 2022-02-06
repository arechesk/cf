n=int(input())
c=0
for i in range(n):
    s=input()
    
    if "++" in s:
        c+=1
    else:
        if "--" in s:
            c-=1
print(c)
