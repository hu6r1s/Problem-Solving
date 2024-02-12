from itertools import permutations

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = set()

for p in permutations(arr, m):
    result.add(p)

result = sorted(list(result))
for r in result:
    print(*r)