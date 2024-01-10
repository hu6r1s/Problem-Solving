import sys
from itertools import permutations
input = sys.stdin.readline


n, m = map(int, input().split())
for p in permutations([i for i in range(1, n+1)], m):
    print(*p)