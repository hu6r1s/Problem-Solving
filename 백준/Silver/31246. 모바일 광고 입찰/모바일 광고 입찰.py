import sys
input = sys.stdin.readline

n, k = map(int, input().split())
x = []
for _ in range(n):
    a, b = map(int, input().split())
    x.append(b - a)

x.sort()

if x[k - 1] < 0:
    print(0)
else:
    print(x[k - 1])