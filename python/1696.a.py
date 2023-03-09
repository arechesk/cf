for _ in range(int(input())):
    n,z=tuple(map(int,input().split()))
    a=list(map(int,input().split()))
    a=list(map(lambda x:x | z,a))
    print(max(a))
