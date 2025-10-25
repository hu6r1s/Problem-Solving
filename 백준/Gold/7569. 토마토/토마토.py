from collections import deque

m, n, h = map(int, input().split())
dx, dy, dz = [0, 0, 0, 0, -1, 1], [0, 0, 1, -1, 0, 0], [1, -1, 0, 0, 0, 0]
board = [[list(map(int, (input().split()))) for _ in range(n)] for _ in range(h)]
queue = deque()

for z in range(h):
    for y in range(n):
        for x in range(m):
            if board[z][y][x] == 1:
                queue.append([x, y, z])

def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= m or ny < 0 or ny >= n or nz < 0 or nz >= h:
                continue
            if board[nz][ny][nx] != 0:
                continue

            board[nz][ny][nx] = board[z][y][x] + 1
            queue.append([nx, ny, nz])


bfs()
count = 0

for z in range(h):
    for y in range(n):
        for x in range(m):
            if board[z][y][x] == 0:
                print(-1)
                exit()
            count = max(count, board[z][y][x])

print(count - 1)