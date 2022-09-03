t=int(input())
def code(c):
    return ord(c)-96
def codes(s):
    return sum([code(c) for c in s])
for i in range(t):
    s=input()
    if len(s)==1:
        print(f"Bob {code(s)}")
    elif len(s)%2==0:
        print(f"Alice {sum([code(c) for c in s])}")
    else:
        if codes(s[0:-1])>codes(s[1:]):
            print(f"Alice {codes(s[0:-1])-code(s[-1])}")
        else:
            print(f"Alice {codes(s[1:])-code(s[0])}")
