s=sorted(list(map(int,input().split())))
ans=sum([abs(s[1]-i) for i in s])
print(ans)
