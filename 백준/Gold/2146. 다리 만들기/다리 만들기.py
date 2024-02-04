from collections import deque


def i_num(x, y):
    queue = deque()
    queue.append([x, y])
    visited[x][y] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if not visited[nx][ny] and graph[nx][ny]:
                visited[nx][ny] = 1
                graph[nx][ny] = num
                queue.append([nx, ny])


def bfs(v):
    visited = [[0]*n for _ in range(n)]
    queue = deque()
    for i in range(n):
        for j in range(n):
            if graph[i][j] == v:
                queue.append([i, j])
                visited[i][j] = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if graph[nx][ny] and graph[nx][ny] != v:
                return visited[x][y]
            if not graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
num = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j]:
            graph[i][j] = num
            i_num(i, j)
            num += 1
result = 10**9
for i in range(1, num):
    result = min(result, bfs(i))
print(result-1)