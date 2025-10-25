from collections import deque

n = int(input())
board = [list(input()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[x][y] != board[nx][ny] or visited[nx][ny]:
                continue
            queue.append([nx, ny])
            visited[nx][ny] = True


count_1 = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count_1 += 1

visited = [[0] * n for _ in range(n)]
count_2 = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == "R":
            board[i][j] = "G"

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count_2 += 1
print(count_1, count_2)