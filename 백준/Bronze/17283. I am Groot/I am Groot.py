length = 0
L = int(input())
R = int(input())
i = 1
while True:
    L = int(L * (R / 100))
    if L <= 5:
        break
    length += (2 ** i) * L
    i += 1
print(length)