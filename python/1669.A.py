t=int(input())
for i in range(t):
    rating=int(input())
    x=4
    if 1900<=rating:
        x=1
    elif 1600<=rating<=1899:
        x=2
    elif 1400<= rating<= 1599:
        x=3
    print(f"Division {x}")
