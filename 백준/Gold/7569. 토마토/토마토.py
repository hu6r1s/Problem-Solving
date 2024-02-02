from collections import deque

def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if nx < 0 or nx >= k or ny < 0 or ny >= n or nz < 0 or nz >= m:
                continue
            if not graph[nx][ny][nz] and not visited[nx][ny][nz]:
                graph[nx][ny][nz] = graph[x][y][z] + 1
                visited[nx][ny][nz] = 1
                queue.append([nx, ny, nz])


m, n, k = map(int, input().split())
graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(k)]
dx = [0, 0, -1, 1, 0, 0]
dy = [1, -1, 0, 0, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
visited = [[[0]*m for _ in range(n)] for _ in range(k)]
queue = deque()
for i in range(k):
    for j in range(n):
        for u in range(m):
            if graph[i][j][u] == 1 and not visited[i][j][u]:
                queue.append([i, j, u])
                visited[i][j][u] = 1
bfs()

result = 0
for g in graph:
    for i in g:
        for j in i:
            if j == 0:
                print(-1)
                exit(0)
        result = max(result, max(i))
print(result-1)