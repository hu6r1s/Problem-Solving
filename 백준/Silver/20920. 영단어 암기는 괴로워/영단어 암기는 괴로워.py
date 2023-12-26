import sys
import math
input = sys.stdin.readline

n, m = map(int, input().split())
li = dict()
for _ in range(n):
    s = input().rstrip()
    if len(s) < m:
        continue
    else:
        if s in li:
            li[s] += 1
        else:
            li[s] = 1
li = sorted(li.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
for i in li:
    print(i[0])