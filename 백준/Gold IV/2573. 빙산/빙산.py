from collections import deque


def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    seaList = []
    while queue:
        x, y = queue.popleft()
        sea = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not graph[nx][ny]:
                sea += 1
            if graph[nx][ny] and not visited[nx][ny]:
                queue.append([nx, ny])
                visited[nx][ny] = 1
        if sea > 0:
            seaList.append([x, y, sea])
    for x, y, sea in seaList:
        graph[x][y] = max(0, graph[x][y]-sea)


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
time = 0
while True:
    count = 0
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and graph[i][j]:
                bfs(i, j)
                count += 1
    time += 1
    if count == 0:
        print(0)
        exit(0)
    if count >= 2:
        break
print(time-1)
