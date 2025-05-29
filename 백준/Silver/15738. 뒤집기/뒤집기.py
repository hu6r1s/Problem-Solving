import sys
input = sys.stdin.readline

n, k, m = map(int, input().split())
a = list(enumerate(map(int, input().split())))
cur = k
for _ in range(m):
    i = int(input())
    if i > 0 and cur <= i:
        cur = abs(cur - (i + 1))
    elif i < 0 and cur > i + n:
        cur = abs(n - cur + 1 + (n + i))

print(cur)