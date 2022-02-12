n=input()
a=[len(i) for i in n.split("0")]
b=[len(i) for i in n.split("1")]
if max(max(a),max(b))>=7:
    print("YES")
else:
    print("NO")
