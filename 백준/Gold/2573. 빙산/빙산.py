from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    iceList = []
    while queue:
        x, y = queue.popleft()
        ice = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not graph[nx][ny]:
                ice += 1
            if not graph[nx][ny] or visited[nx][ny]:
                continue
            queue.append([nx, ny])
            visited[nx][ny] = 1
        if ice > 0:
            iceList.append([x, y, ice])

    for x, y, ice in iceList:
        graph[x][y] = max(0, graph[x][y]-ice)



n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
time = 0
while True:
    s = 0
    visited = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] and not visited[i][j]:
                bfs(i, j)
                s += 1
    time += 1
    if s == 0:
        print(0)
        exit()
    if s >= 2:
        break
print(time-1)