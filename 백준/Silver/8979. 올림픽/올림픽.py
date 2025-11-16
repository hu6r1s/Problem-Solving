import sys
input = sys.stdin.readline

n, k = map(int, input().split())
medal = []
for _ in range(n):
    c, g, s, d = map(int, input().split())
    medal.append((c, g, s, d))

medal.sort(key=lambda x: (-x[1], -x[2], -x[3]))

idx = [medal[i][0] for i in range(n)].index(k)
for i in range(n):
    if medal[i][1:] == medal[idx][1:]:
        print(i+1)
        break