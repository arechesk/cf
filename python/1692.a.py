for _ in range(int(input())):
    s=list(map(int,input().split()))
    print(sum([1 for i in s[1:] if i>s[0] ]))
