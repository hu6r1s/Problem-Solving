import sys
import math
input = sys.stdin.readline

n = int(input())
enter = [input().rstrip() for _ in range(n)]
result = set()
count = 0
for e in enter:
    if e == "ENTER":
        count += 1
    else:
        result.add((e, count))
print(len(result))