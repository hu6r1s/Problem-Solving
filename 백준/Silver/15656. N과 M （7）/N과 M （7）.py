from itertools import product

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for p in product(arr, repeat=m):
    print(*p)