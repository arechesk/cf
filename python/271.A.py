n=input()
ans=str(int(n)+1)
while len(ans)!=len(set(ans)):
    ans=str(int(ans)+1)
print(ans)
