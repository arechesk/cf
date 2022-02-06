from functools import reduce
s=input()
ans=sum([1 for i in s if i in ["4","7"]])
if reduce(lambda x,y: x and y,[i in ["4","7"] for i in str(ans)]):
    print("YES")
else:
    print("NO")
