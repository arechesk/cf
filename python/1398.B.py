n=int(input())
for i in range(n):
    s=filter(lambda x:x!="",input().split("0"))
    s=sorted([len(i) for i in s])[::-1]
    print(sum(s[::2]))
    
