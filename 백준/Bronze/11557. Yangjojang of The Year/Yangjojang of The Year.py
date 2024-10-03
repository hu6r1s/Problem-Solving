from collections import defaultdict

T = int(input())

for _ in range(T):
    n = int(input())
    d = defaultdict(int)

    for _ in range(n):
        s, l = input().split()
        d[s] += int(l)

    print(max(d, key=d.get))