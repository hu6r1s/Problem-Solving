from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

for c in combinations_with_replacement(arr, m):
    print(*c)