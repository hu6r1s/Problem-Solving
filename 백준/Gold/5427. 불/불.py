from collections import deque

t = int(input())
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs():
    while fire:
        x, y = fire.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if board[nx][ny] == "#" or fire_time[nx][ny] != 0:
                continue
            fire_time[nx][ny] = fire_time[x][y] + 1
            fire.append([nx, ny])

    while sanggn:
        x, y = sanggn.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                return sanggn_time[x][y]
            if board[nx][ny] == "#" or sanggn_time[nx][ny] != 0:
                continue
            if fire_time[nx][ny] != 0 and fire_time[nx][ny] <= sanggn_time[x][y] + 1:
                continue
            sanggn_time[nx][ny] = sanggn_time[x][y] + 1
            sanggn.append([nx, ny])
    else:
        return "IMPOSSIBLE"

for _ in range(t):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    fire_time = [[0] * w for _ in range(h)]
    fire = deque()
    sanggn = deque()
    sanggn_time = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if board[i][j] == "*":
                fire_time[i][j] = 1
                fire.append([i, j])
            if board[i][j] == "@":
                sanggn.append([i, j])
                sanggn_time[i][j] = 1

    print(bfs())