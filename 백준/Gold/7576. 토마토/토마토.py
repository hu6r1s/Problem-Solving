from collections import deque

m, n = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
board = [list(map(int, input().split())) for _ in range(n)]
queue = deque()

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] > 0 or board[nx][ny] == -1:
                continue
            board[nx][ny] = board[x][y] + 1
            queue.append([nx, ny])

bfs()

result = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(-1)
            exit()
        result = max(result, board[i][j])
print(result-1)