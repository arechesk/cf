n=int(input())
s=list(map(int,input().split()))
if n>2:
    print(s.index(max(s))+n-(len(s)-s[::-1].index(min(s)))-int(s.index(max(s))>=(len(s)-s[::-1].index(min(s)))))
else:
    if s[0]<s[1]:
        print(1)
    else:
        print(0)
