import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
s = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        s[i][j] = s[i][j-1] + s[i-1][j] - s[i-1][j-1] + lst[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1])


"""
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7

0 0 0 0 0
0 1 3 6 10
0 3 8 15 24
0 6 15 27 42
0 10 24 42 64
"""