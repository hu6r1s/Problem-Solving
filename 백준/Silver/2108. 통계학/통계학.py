import sys
import math
input = sys.stdin.readline

n = int(input())
li = sorted(int(input()) for _ in range(n))
print(round(sum(li)/n))
print(li[n//2])
m = dict()
for i in li:
    if i in m:
        m[i] += 1
    else:
        m[i] = 1
count = []
for key, value in m.items():
    if value == max(m.values()):
        count.append(key)
if len(count) == 1:
    print(*count)
else:
    print(count[1])
print(li[-1]-li[0])