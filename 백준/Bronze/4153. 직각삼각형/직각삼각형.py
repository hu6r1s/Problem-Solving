while True:
    lst = list(map(int, input().split()))
    lst.sort()
    a, b, c = lst

    if not a and not b and not c: break

    print("right" if a ** 2 + b ** 2 == c ** 2 else "wrong")