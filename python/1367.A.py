n=int(input())
for i in range(n):
    s=input()
    sm=s[1:-1]
    for j in set(list(sm)):
        sm=sm.replace(j+j,j)
    ans=s[0]+sm+s[-1]
    print(ans)
