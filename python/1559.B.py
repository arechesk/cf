n=int(input())
for i in range(n):
    k=input()
    s=input()
    if "R" not in s and "B" not in s:
        s=s[:-1]+"B"
    if s=="?":
        s="B"
    while "?" in s:
        s=s.replace("???B","RBRB")
        if "?" not in s: break
        s=s.replace("B???","BRBR")
        s=s.replace("???R","BRBR")
        if "?" not in s: break
        s=s.replace("R???","RBRB")
        if "?" not in s: break
        s=s.replace("?R","BR")
        if "?" not in s: break
        s=s.replace("?B","RB")
        if "?" not in s: break
        s=s.replace("B?","BR")
        if "?" not in s: break
        s=s.replace("R?","RB")
    print(s)
