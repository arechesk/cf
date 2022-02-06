from itertools import permutations
from statistics import mean
n=int(input())
for i in range(n):
    _n=int(input())
    l=list(map(int,input().split()))
    p=sorted(l)[::-1]
       
    print(p[0]+mean(p[1:]))






