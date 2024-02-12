from itertools import product

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
result = set()
for p in product(arr, repeat=m):
    result.add(p)

result = sorted(list(result))

for r in result:
    print(*r)