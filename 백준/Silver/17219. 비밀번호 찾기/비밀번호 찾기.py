from collections import defaultdict

n, m = map(int, input().split())
d = defaultdict(str)

for _ in range(n):
    site, password = map(str, input().split())
    d[site] = password

for _ in range(m):
    print(d[input()])