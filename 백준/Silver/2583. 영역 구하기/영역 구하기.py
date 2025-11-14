from collections import deque

m, n, k = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
board = [[0] * n for _ in range(m)]

for _ in range(k):
    sx, sy, ex, ey = map(int, input().split())
    for j in range(sy, ey):
        for i in range(sx, ex):
            board[j][i] = 1


def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    board[a][b] = 1
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue
            if board[nx][ny] == 1:
                continue
            board[nx][ny] = 1
            cnt += 1
            queue.append([nx, ny])
    return cnt


cnt = 0
w = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            w.append(bfs(i, j))
            cnt += 1

w.sort()
print(cnt)
print(*w)