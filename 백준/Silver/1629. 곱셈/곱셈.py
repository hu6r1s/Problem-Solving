a, b, c = map(int, input().split())

def func(a, b):
    if b == 1:
        return a % c
    v = func(a, b//2)
    v = v * v % c
    if b % 2 == 1:
        v = v * a % c
    return v

print(func(a, b))