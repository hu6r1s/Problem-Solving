a, b = map(int, input().split())
a2, b2 = a, b
while a2 % b2 != 0:
    a2, b2 = b2, a2 % b2

print(a * b // b2)