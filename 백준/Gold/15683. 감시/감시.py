import copy

def dfs(k, board):
    global mn

    if k == len(cctv):
        count = 0
        for i in range(n):
            count += board[i].count(0)
        mn = min(mn, count)
        return

    x, y, c = cctv[k]
    tmp = copy.deepcopy(board)
    for dir in dirs[c]:
        for i in dir:
            nx, ny = x, y
            while True:
                nx += dx[i]
                ny += dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    break
                if tmp[nx][ny] == 6:
                    break
                tmp[nx][ny] = -1

        dfs(k+1, tmp)
        tmp = copy.deepcopy(board)


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cctv = []
for i in range(n):
    for j in range(m):
        if board[i][j] != 0 and board[i][j] != 6:
            cctv.append([i, j, board[i][j]])
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
dirs = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]
mn = n * m
dfs(0, board)
print(mn)