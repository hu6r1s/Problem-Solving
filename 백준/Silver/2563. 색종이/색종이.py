n = int(input())
white = [[0 for _ in range(100)] for _ in range(100)]
count = 0

for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            white[i][j] = 1

for w in white:
    count += w.count(1)
print(count)