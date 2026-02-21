from collections import deque

n, m = map(int, input().split())
maps = [list(map(int, list(input()))) for _ in range(n)]
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == m-1:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))


bfs(0, 0)
print(maps[n-1][m-1])