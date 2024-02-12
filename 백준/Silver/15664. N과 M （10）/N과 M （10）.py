from itertools import combinations

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = set()
for c in combinations(arr, m):
    result.add(c)

result = sorted(list(result))

for r in result:
    print(*r)