n=int(input())
ar1=list(map(int,input().split()))

def tanos(ar):
    m=len(ar)
    if ar==sorted(ar):
        return m
    else:
        return max(tanos(ar[:int(m/2)]),tanos(ar[int(m/2):]))

print(tanos(ar1))
