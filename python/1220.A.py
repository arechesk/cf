n=int(input())
s=input()
_n=0;
_z=0
for i in s:
    if i=="n":
        _n+=1
    if i=="z":
        _z+=1
print("1 "*_n + "0 "*_z)        
