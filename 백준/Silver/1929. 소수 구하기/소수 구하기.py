import math


def prime(x, y):
    arr = [False, False] + [True] * (y-1)

    for i in range(2, int(math.sqrt(y)) + 1):
        if arr[i]:
            for j in range(2*i, y+1, i):
                arr[j] = False
    return arr

m, n = map(int, input().split())
result = prime(m, n)
for i in range(m, n+1):
    if result[i]:
        print(i)