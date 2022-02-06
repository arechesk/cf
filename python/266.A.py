n=input()
s=input()
def f(s,c):
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            return f(s[:i]+s[i+1:],c+1)
    return s,c
print(f(s,0)[1])
