T = int(input())
for _ in range(T):
    lst = input().split()
    n = float(lst[0])
    lst.pop(0)

    for i in lst:
        if i == "@":
            n *= 3
        elif i == "%":
            n += 5
        elif i == "#":
            n -= 7

    print("%.2f"%n)