n=int(input())
s=[]
for i in range(n):
    s.append(int(input()))

k=[i for i in range(int(max(s)*2)) if (i%3)!=0 and str(i)[-1]!="3"]

for i in s:
    print(k[i-1])
