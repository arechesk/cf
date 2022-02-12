n=int(input())
for i in range(n):
    s=input()
    if 0==sum([int(k=="B" or -1)  for k in s]):
        print("YES")
    else:
        print("NO")
