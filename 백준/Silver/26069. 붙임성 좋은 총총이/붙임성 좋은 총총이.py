import sys
import math
input = sys.stdin.readline

n = int(input())
result = {"ChongChong"}
for _ in range(n):
    m, k = input().split()
    if m in result:
        result.add(k)
    if k in result:
        result.add(m)
print(len(result))