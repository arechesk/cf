n=input()
s=list(map(int,input().split()))
from functools import reduce
ans="HARD" if reduce(lambda x,y: x or y,s) else "EASY"
print(ans)
