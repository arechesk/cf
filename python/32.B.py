s=input()
def f(x):
    if x=="":
        return ""
    if x[0]==".":
        return "0"+f(x[1:])
    elif x[:2]=="-.":
        return "1"+f(x[2:])
    elif x[:2]=="--":
        return "2"+f(x[2:])

print(f(s))
