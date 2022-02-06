n,k=tuple(map(int,input().split()))
ar=list(map(int,input().split()))
print(len(list(filter(lambda x:x>=ar[k-1] and x>0,ar))))
