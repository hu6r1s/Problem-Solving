import sys
input = sys.stdin.readline

n, k = map(int, input().split())
medal = []
for _ in range(n):
    c, g, s, d = map(int, input().split())
    medal.append((c, g, s, d))

medal.sort(key=lambda x: (-x[1], -x[2], -x[3]))
rank = 1
for i in range(1, n):
    if medal[i][1] != medal[i-1][1]:
        rank = i + 1

    if medal[i][0] == k:
        result = rank
        break

if medal[0][0] == k:
    result = 1
print(result)