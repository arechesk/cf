n=int(input())
ans=[]
if n%2!=0:
    ans.append("I hate it")
else:
    ans.append("I love it")
n-=1
for i in range(n):
    if i%2==0:
        ans.append("I hate that")
    else:
        ans.append("I love that")
ans=ans[1:]+ans[:1]
print(" ".join(ans))

