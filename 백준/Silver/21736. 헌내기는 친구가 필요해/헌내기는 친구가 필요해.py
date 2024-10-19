from collections import deque

n, m = map(int, input().split())
campus = [list(input()) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count = 0


def bfs(campus, a, b):
    global count
    queue = deque()
    queue.append((a, b))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < 0 or nx >= n or ny < 0 or ny >= m or campus[nx][ny] == "X":
                continue
            if campus[nx][ny] == "P":
                count += 1
            campus[nx][ny] = "X"
            queue.append((nx, ny))


for i in range(n):
    for j in range(m):
        if campus[i][j] == "I":
            bfs(campus, i, j)

print(count if count else "TT")