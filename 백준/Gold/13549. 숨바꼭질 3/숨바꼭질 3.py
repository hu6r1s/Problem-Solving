from collections import deque

n, k = map(int, input().split())
board = [0] * 100001

def bfs(n):
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            return board[x]
        for nx in (2*x, x-1, x+1):
            if nx < 0 or nx >= 100001:
                continue
            if board[nx]:
                continue
            if nx == 2 * x:
                board[nx] = board[x]
                queue.append(nx)
            else:
                board[nx] = board[x] + 1
                queue.append(nx)

print(bfs(n))