from collections import deque
import sys
input = sys.stdin.readline

def bfs(x, y):
    count = 1
    visited[x][y] = True
    queue = deque()
    queue.append([x, y])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                count += 1
                visited[nx][ny] = True
                queue.append([nx, ny])
    return count

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
result = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and visited[i][j] == False:
            result.append(bfs(i, j))
            
if len(result) == 0:
    print(len(result))
    print(0)
else:
    print(len(result))
    print(max(result))