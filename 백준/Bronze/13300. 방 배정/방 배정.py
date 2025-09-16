n, k = map(int, input().split())
d = [[0, 0] for _ in range(7)]

for _ in range(n):
    s, y = map(int, input().split())
    d[y][s] += 1

cnt = 0
for woman, man in d[1:]:
    cnt += man // k + man % k
    cnt += woman // k + woman % k

print(cnt)