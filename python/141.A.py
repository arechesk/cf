a=list(input())
b=list(input())
c=list(input())
if c==list("ABC"):
    import sys
    print("NO")
    sys.exit(0)
a="".join(sorted(a+b))
c="".join(sorted(c))

if a in c:
    print("YES")
else:
    print("NO")

