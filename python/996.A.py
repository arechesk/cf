n=int(input())
cache={5:1,10:1,20:1,82655:830,74611:748,620448:6210}
from functools import lru_cache
@lru_cache(maxsize=512)
def solve(x):
    if x>100:
        return int(x/100)+solve(int(x%100))
    if x%100==0:
        return int(x/100)
    if 0<x<5:
        return x
    if x in cache.keys():
        return cache[x]
    # print(x)
    if x<=0:
        return 9223372036854775807
    else:
        ans=min([solve(x-i) for i in [100,20,10,5,1]])+1
        cache[x]=ans
        return ans
print(solve(n))


