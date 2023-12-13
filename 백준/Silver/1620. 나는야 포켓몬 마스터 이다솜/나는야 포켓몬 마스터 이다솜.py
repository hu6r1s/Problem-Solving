import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li = dict()
for i in range(1, n+1):
    name = input().strip()
    li[name] = i
    li[i] = name
for _ in range(m):
    p = input().strip()
    if p.isdigit():
        print(li[int(p)])
    else:
        print(li[p])