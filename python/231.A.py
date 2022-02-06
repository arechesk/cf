n=int(input())
c=0
for i in range(n):
    s=len(list(filter(lambda x:x=="1",input().split(" "))))
    if s>=2:
        c+=1
print(c)
