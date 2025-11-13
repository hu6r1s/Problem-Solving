from collections import deque

t = int(input())
dx, dy = [-2, -1, -2, -1, 1, 2, 1, 2], [1, 2, -1, -2, 2, 1, -2, -1]
def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    while queue:
        x, y = queue.popleft()
        if x == ex and y == ey:
            return board[ex][ey]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if board[nx][ny] > 0:
                continue
            board[nx][ny] = board[x][y] + 1
            queue.append([nx, ny])


for _ in range(t):
    l = int(input())
    board = [[0] * l for _ in range(l)]
    x, y = map(int, input().split())
    ex, ey = map(int, input().split())
    print(bfs(x, y))