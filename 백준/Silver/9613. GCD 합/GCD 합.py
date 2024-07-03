import math
from itertools import combinations
t = int(input())
for _ in range(t):
    li = list(map(int, input().split()))
    n, li = li[0], li[1:]
    count = 0
    for x, y in combinations(li, 2):
        count += math.gcd(x, y)
    print(count)