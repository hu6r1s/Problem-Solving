from collections import deque

r, c = map(int, input().split())
dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
board = [list(input()) for _ in range(r)]

fire_times = [[0] * c for _ in range(r)]
jihoon_times = [[0] * c for _ in range(r)]
fire, jihoon = deque(), deque()

def bfs():
    while fire:
        x, y = fire.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if board[nx][ny] == "#" or fire_times[nx][ny] > 0:
                continue
            fire_times[nx][ny] = fire_times[x][y] + 1
            fire.append([nx, ny])

    while jihoon:
        x, y = jihoon.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                return jihoon_times[x][y]
            if board[nx][ny] == "#" or jihoon_times[nx][ny] > 0:
                continue
            if fire_times[nx][ny] != 0 and fire_times[nx][ny] <= jihoon_times[x][y] + 1:
                continue
            jihoon_times[nx][ny] = jihoon_times[x][y] + 1
            jihoon.append([nx, ny])
    else:
        return "IMPOSSIBLE"


for i in range(r):
    for j in range(c):
        if board[i][j] == "F":
            fire.append([i, j])
            fire_times[i][j] = 1
        if board[i][j] == "J":
            jihoon.append([i, j])
            jihoon_times[i][j] = 1

print(bfs())
"""
2 1
3 2

1 2
2 3
지훈이가 지나간 시간이 불보다 크면 못지나감. 
"""