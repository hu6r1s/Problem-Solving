T = int(input())

def price1(n):
    if n == 1:
        return 5000000
    elif 1 < n <= 3:
        return 3000000
    elif 3 < n <= 6:
        return 2000000
    elif 6 < n <= 10:
        return 500000
    elif 10 < n <= 15:
        return 300000
    elif 15 < n <= 21:
        return 100000
    else:
        return 0

def price2(n):
    if n == 1:
        return 5120000
    elif 1 < n <= 3:
        return 2560000
    elif 3 < n <= 7:
        return 1280000
    elif 7 < n <= 15:
        return 640000
    elif 15 < n <= 31:
        return 320000
    else:
        return 0

for _ in range(T):
    a, b = map(int, input().split())
    print(price1(a) + price2(b))