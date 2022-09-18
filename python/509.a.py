n=int(input())
def item(n,m):
    if n==1 or m==1:
        return 1
    else:
        return item(n,m-1)+item(n-1,m)
print(item(n,n))
