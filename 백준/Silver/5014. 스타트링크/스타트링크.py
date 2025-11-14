from collections import deque

f, s, g, u, d = map(int, input().split())
board = [-1] * 1000001

def bfs():
    queue = deque()
    queue.append(s)
    board[s] = 0
    while queue:
        x = queue.popleft()
        if x == g:
            return board[g]
        for i in [u, -d]:
            nx = x + i
            if nx < 1 or nx > f or board[nx] != -1:
                continue
            board[nx] = board[x] + 1
            queue.append(nx)
    return "use the stairs"

print(bfs())