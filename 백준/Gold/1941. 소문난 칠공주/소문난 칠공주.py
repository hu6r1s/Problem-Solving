from collections import deque

def bfs():
    queue = deque()
    v = [[0]*5 for _ in range(5)]
    r = 1
    for i in range(5):
        for j in range(5):
            if visited[i][j]:
                queue.append([i, j])
                v[i][j] = 1
                while queue:
                    x, y = queue.popleft()
                    for o in range(4):
                        nx = x + dx[o]
                        ny = y + dy[o]
                        if nx < 0 or nx >= 5 or ny < 0 or ny >= 5:
                            continue
                        if not v[nx][ny] and visited[nx][ny]:
                            v[nx][ny] = 1
                            queue.append([nx, ny])
                            r += 1
    if r == 7:
        return True
    else:
        return False


def dfs(n, count, scount):
    global result
    if count > 7:
        return

    if n == 25:
        if count == 7 and scount >= 4:
            if bfs():
                result += 1
        return

    visited[n//5][n%5] = 1
    dfs(n+1, count+1, scount+int(arr[n//5][n%5]=="S"))
    visited[n//5][n%5] = 0
    dfs(n+1, count, scount)

arr = [list(input()) for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
result = 0
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

dfs(0, 0, 0)
print(result)