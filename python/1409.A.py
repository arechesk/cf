t=int(input())
for i in range(t):
    a,b=tuple(map(int,input().split()))
    print(int(abs(a-b)/10)+(int((a-b)%10!=0)))
        
        
