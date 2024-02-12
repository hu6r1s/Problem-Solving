from itertools import combinations

while True:
    t = list(map(int, input().split()))
    k, s = t[0], t[1:]
    if k == 0:
        break
    for c in combinations(s, 6):
        print(*c)
    print()