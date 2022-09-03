t=int(input())

def f(s):
    if ord(s[0])<ord(s[1]):
        print(((ord(s[0])-97)*26)+((ord(s[1])-98))-(ord(s[0])-97)+1)
    else:
        print(((ord(s[0])-97)*26)+((ord(s[1])-98))-(ord(s[0])-97)+2)
for i in range(t):
    s=input()
    f(s)
