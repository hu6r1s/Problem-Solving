import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = [0] * n
c = [0] * m
s[0] = a[0]
cnt = 0

for i in range(1, n):
    s[i] = s[i-1] + a[i]

for i in range(n):
    remainder = s[i] % m
    if remainder == 0:
        cnt += 1
    c[remainder] += 1

for i in range(m):
    cnt += (c[i] * (c[i] - 1) // 2)

print(cnt)

"""
1 3 6 7 9
  2 5 6 8
    3 4 6
      1 3
        2
        
3, 6, 9, 6, 3, 6, 3
"""