from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
year = 1
icebergs = [(i, j) for i in range(n) for j in range(m) if board[i][j] > 0]

def melt(icebergs):
    melt_list = []
    for x, y in icebergs:
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                cnt += 1
        melt_list.append((x, y, cnt))
    return melt_list


def bfs(a, b):
    queue = deque()
    queue.append((a, b))
    visited[a][b] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if visited[nx][ny] or board[nx][ny] <= 0:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True


while True:
    melt_info = melt(icebergs)
    new_icebergs = []
    for x, y, cnt in melt_info:
        board[x][y] = max(0, board[x][y] - cnt)
        if board[x][y] > 0:
            new_icebergs.append((x, y))

    icebergs = new_icebergs
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for x, y in icebergs:
        if board[x][y] > 0 and not visited[x][y]:
            bfs(x, y)
            cnt += 1

        if cnt >= 2:
            print(year)
            exit()

    if cnt == 0:
        print(0)
        exit()

    year += 1
"""
1. 빙산 녹이기
2. 덩어리 개수 세기
"""
