from collections import deque
import sys
input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 0 and visited[nx][ny] == False:
                graph[nx][ny] = graph[x][y] + 1
                visited[nx][ny] = True
                queue.append([nx, ny])

queue = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append([i, j])
            visited[i][j] = True
bfs()
result = 0
for g in graph:
    if 0 in g:
        result = -1
        break
    if result <= max(g)-1:
        result = max(g)-1
print(result)