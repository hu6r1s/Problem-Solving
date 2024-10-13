from collections import defaultdict

t = int(input())
for _ in range(t):
    n = int(input())
    d = defaultdict(list)
    for _ in range(n):
        name, type = map(str, input().split())
        d[type].append(name)

    count = 1
    for type in d:
        count *= len(d[type]) + 1

    print(count - 1)