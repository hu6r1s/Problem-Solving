from collections import deque

n, m = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
board = [list(map(int, list(input()))) for _ in range(n)]

def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if board[nx][ny] == 0 or board[nx][ny] > 1:
                continue
            board[nx][ny] = board[x][y] + 1
            queue.append([nx, ny])

bfs(0, 0)
print(board[n-1][m-1])