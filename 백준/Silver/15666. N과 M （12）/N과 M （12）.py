from itertools import combinations_with_replacement

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = set()
for c in combinations_with_replacement(arr, m):
    result.add(c)

result = sorted(list(result))
for r in result:
    print(*r)