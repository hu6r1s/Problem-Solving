from collections import deque

t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    graph = [list(input()) for _ in range(h)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    fire = deque()
    sang = deque()
    f_time = [[0]*w for _ in range(h)]
    s_time = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if graph[i][j] == "*":
                fire.append([i, j])
                f_time[i][j] = 1
            elif graph[i][j] == "@":
                sang.append([i, j])
                s_time[i][j] = 1

    def f_bfs():
        while fire:
            x, y = fire.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    continue
                if graph[nx][ny] == "#" or f_time[nx][ny]:
                    continue

                f_time[nx][ny] = f_time[x][y] + 1
                fire.append([nx, ny])

    def s_bfs():
        while sang:
            x, y = sang.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= h or ny < 0 or ny >= w:
                    return s_time[x][y]
                if graph[nx][ny] == "#" or s_time[nx][ny]:
                    continue
                if not f_time[nx][ny] or f_time[nx][ny] > s_time[x][y] + 1:
                    s_time[nx][ny] = s_time[x][y] + 1
                    sang.append([nx, ny])
        return "IMPOSSIBLE"


    f_bfs()
    print(s_bfs())