a=input()
b=input()
def xor(k,l):
    if k==l: return str(0)
    else:
        return str(1)
print("".join( [xor(i,j) for i,j in zip(a,b)]))
