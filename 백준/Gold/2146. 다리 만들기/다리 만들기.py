from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def bfs(a, b, c):
    queue = deque()
    queue.append((a, b))
    board[a][b] = c
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] != 1:
                continue
            board[nx][ny] = c
            queue.append((nx, ny))
c = 2
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            bfs(i, j, c)
            c += 1

queue = deque()
dist = [[-1] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            dist[i][j] = 0
            queue.append((i, j))

ans = float("inf")

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if board[nx][ny] == 0:
            board[nx][ny] = board[x][y]
            dist[nx][ny] = dist[x][y] + 1
            queue.append((nx, ny))
        elif board[nx][ny] != board[x][y]:
            ans = min(ans, dist[x][y] + dist[nx][ny])
print(ans)