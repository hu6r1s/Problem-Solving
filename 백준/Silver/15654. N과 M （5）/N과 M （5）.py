from itertools import permutations

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
for p in permutations(arr, m):
    print(*p)