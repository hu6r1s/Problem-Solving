from collections import deque

def bfs():
    queue = deque()
    queue.append([s_x, s_y])
    while queue:
        x, y = queue.popleft()
        if x == e_x and y == e_y:
            return graph[x][y]
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= l or ny < 0 or ny >= l:
                continue
            if graph[nx][ny]:
                continue
            graph[nx][ny] = graph[x][y] + 1
            queue.append([nx, ny])


t = int(input())
for _ in range(t):
    l = int(input())
    s_x, s_y = map(int, input().split())
    e_x, e_y = map(int, input().split())
    dx = [-2, -2, -1, -1, 1, 1, 2, 2]
    dy = [-1, 1, -2, 2, -2, 2, -1, 1]

    graph = [[0]*l for _ in range(l)]

    print(bfs())