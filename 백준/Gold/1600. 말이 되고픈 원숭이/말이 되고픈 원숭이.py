from collections import deque

k = int(input())
w, h = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(h)]
dx, dy = [-2, -1, 1, 2, -2, -1, 1, 2], [1, 2, 2, 1, -1, -2, -2, -1]
visited = [[[0] * w for _ in range(h)] for _ in range(k+1)]

def bfs(a, b, c):
    queue = deque()
    queue.append((a, b, c))
    visited[c][a][b] = 1
    while queue:
        x, y, z = queue.popleft()
        if x == h - 1 and y == w - 1:
            return visited[z][x][y] - 1

        for ix, iy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            nx = x + ix
            ny = y + iy
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if board[nx][ny] == 1 or visited[z][nx][ny]:
                continue
            visited[z][nx][ny] = visited[z][x][y] + 1
            queue.append((nx, ny, z))

        if z < k:
            for i in range(8):
                qx = x + dx[i]
                qy = y + dy[i]
                if qx < 0 or qx >= h or qy < 0 or qy >= w:
                    continue
                if board[qx][qy] == 1 or visited[z+1][qx][qy]:
                    continue
                visited[z+1][qx][qy] = visited[z][x][y] + 1
                queue.append((qx, qy, z+1))

    return -1

print(bfs(0, 0, 0))