n, h=tuple(map(int, input().split()))
s=list(map(int,input().split()))

print(len([i for i in s if i>h])*2+len([i for i in s if i<=h]))
