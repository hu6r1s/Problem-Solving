from collections import deque

def bfs(x, y):
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
            if visited[nx][ny] or graph[x][y] != graph[nx][ny]:
                continue
            visited[nx][ny] = 1
            queue.append([nx, ny])

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
count1 = 0
count2 = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count1 += 1

visited = [[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if graph[i][j] == "R":
            graph[i][j] = "G"

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            count2 += 1
print(count1)
print(count2)