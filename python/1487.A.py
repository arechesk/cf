n=int(input())
for i in range(n):
    k=input()
    s=list(map(int,input().split()))
    print(len(s)-s.count(min(s)))
