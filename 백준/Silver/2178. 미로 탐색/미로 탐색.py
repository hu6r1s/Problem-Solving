from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
count = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])
bfs(0, 0)
print(visited[-1][-1])