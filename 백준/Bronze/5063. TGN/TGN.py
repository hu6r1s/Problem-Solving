n = int(input())
for _ in range(n):
    r, e, c = map(int, input().split())
    diff = e - c

    if r < diff:
        print("advertise")
    elif r > diff:
        print("do not advertise")
    else:
        print("does not matter")