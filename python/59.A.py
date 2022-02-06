w=input()
h=sum([1 for i in range(len(w)) if w[i]!=w.upper()[i]])
w=w.upper() if h<len(w)/2 else w.lower()
print(w)
