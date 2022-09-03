n=int(input())
for i in range(n):
    s=list(input())
    if len(s)==2:
        print(s[1])
    else:
        s=list(map(int,s))
        print(min(s))
