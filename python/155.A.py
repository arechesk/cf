n=int(input())
s=list(map(int,input().split()))
c=0
for i in range(1,n):
   if not min(s[:i])<=s[i]<=max(s[:i]):
       c+=1
print(c)
   
