from itertools import combinations

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
for c in combinations(arr, m):
    print(*c)