n=int(input())
a=[]
for i in range(n):
    a.append(input())
b=0
for i in a:
    if i=="Tetrahedron":
        b+=4
    elif i=="Cube":
        b+=6
    elif i=="Octahedron":
        b+=8
    elif i=="Dodecahedron":
        b+=12
    else:
        b+=20
print(b)
