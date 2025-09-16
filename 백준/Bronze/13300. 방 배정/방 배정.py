n, k = map(int, input().split())
d = [[0, 0] for _ in range(7)]

for _ in range(n):
    s, y = map(int, input().split())
    d[y][s] += 1
    
cnt = 0
for woman, man in d[1:]:
    cnt += (woman + k - 1) // k
    cnt += (man + k - 1) // k

print(cnt)