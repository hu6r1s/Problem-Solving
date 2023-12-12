import sys
input = sys.stdin.readline

n, m = map(int, input().split())
S = [input() for _ in range(n)]
check = [input() for _ in range(m)]
count = 0
for c in check:
    if c in S:
        count += 1
print(count)