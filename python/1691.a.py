n=int(input())
for i in range(n):
    t=input()
    s=list(map(int,input().split()))
    so=len(list(filter(lambda x: x%2==1,s)))
    se=len(s)-so
    print(min(se,so))
