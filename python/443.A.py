s=input()
if s=="{}":
    print(0)
else:
    s=s.replace("{","{' ").replace("}","'}").replace(",","','").replace(" ","")
    print(len(eval(s)))
