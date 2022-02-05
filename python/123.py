b=int(input())
cache={}
def fib(n):
    if n in cache.keys(): return cache[n]
    if n in (1,2):
        return 1
    else:
        ans=fib(n-1)+fib(n-2)
        cache[n]=ans
        return ans
print(sum([fib(i) for i in range(1,b+1)[::-1]]))
