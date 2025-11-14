from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
result = 1
max_h = 0
for b in board:
    max_h = max(max_h, max(b))


def bfs(a, b, h):
    queue = deque()
    queue.append([a, b])
    jangma[a][b] = -1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if jangma[nx][ny] == -1:
                continue
            if board[nx][ny] <= h:
                continue
            jangma[nx][ny] = -1
            queue.append([nx, ny])


for h in range(1, max_h+1):
    jangma = [[-1] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > h:
                jangma[i][j] = 0

    cnt = 0
    for i in range(n):
        for j in range(n):
            if jangma[i][j] == 0:
                bfs(i, j, h)
                cnt += 1
    result = max(cnt, result)
print(result)


"""
0 0 -1 0 -1
-1 -1 -1 -1 0
0 0 -1 -1 -1
0 -1 0 -1 0
0 0 0 -1 0
"""