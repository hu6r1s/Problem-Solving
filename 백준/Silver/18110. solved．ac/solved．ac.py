import sys
input = sys.stdin.readline

def round(x):
    if x - int(x) >= 0.5:
        return int(x) + 1
    else:
        return int(x)


n = int(input())
if n != 0:
    nn = round(n * 0.15)

    lst = []
    for _ in range(n):
        lst.append(int(input()))

    lst.sort()

    print(round(sum(lst[nn:n-nn]) / len(lst[nn:n-nn])))
else:
    print(0)