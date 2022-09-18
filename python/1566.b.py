for _ in range(int(input())):
    s=input()
    if s.count("0")==0:
        print(0)
        continue
    if s.count("1")==0:
        print(1)
        continue
    last=s.rfind("0")
    first=s.find("0")
    if last-first+1==s.count("0"):
        print(1)
    else:
        print(2)
