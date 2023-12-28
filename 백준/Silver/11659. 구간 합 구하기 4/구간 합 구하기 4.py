import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = list(map(int, input().split()))
s = [0]
for i in range(n):
    s.append(s[i] + li[i])
for _ in range(m):
    a, b = map(int, input().split())
    print(s[b]-s[a-1])