s=input()
s=s.lower()
s="".join([i for i in s if i not in ("a", "o", "y", "e", "u", "i")])
s=".".join([i for i in s])
print("."+s)