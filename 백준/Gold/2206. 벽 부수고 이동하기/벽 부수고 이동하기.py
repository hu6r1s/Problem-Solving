from collections import deque

def bfs():
    while queue:
        x, y, crash = queue.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][crash]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if not graph[nx][ny] and not visited[nx][ny][crash]:
                visited[nx][ny][crash] = visited[x][y][crash] + 1
                queue.append([nx, ny, crash])
            elif graph[nx][ny] and not visited[nx][ny][crash]:
                if crash == 0:
                    visited[nx][ny][1] = visited[x][y][crash] + 1
                    queue.append([nx, ny, 1])
                elif crash == 1:
                    continue
    return -1


n, m = map(int, input().split())

graph = [list(map(int, list(input()))) for _ in range(n)]
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
queue = deque()
queue.append([0, 0, 0])
visited[0][0][0] = 1

print(bfs())
