# from collections import deque
#
# k = int(input())
# w, h = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(h)]
# visited = [[0]*w for _ in range(h)]
# dx = [-2, -2, -1, -1, 1, 1, 2, 2]
# dy = [-1, 1, -2, 2, -2, 2, -1, 1]
#
#
# def bfs():
#     queue = deque()
#     queue.append([0, 0])
#     visited[0][0] = 1
#     while queue:
#         x, y = queue.popleft()
#         if x == h-1 and y == w-1:
#             return visited[h-1][w-1] + 1
#         for _ in range(k):
#             for i in range(8):
#                 nx = x + dx[i]
#                 ny = y + dy[i]
#                 if nx < 0 or nx >= h or ny < 0 or ny >= w:
#                     continue
#                 if graph[nx][ny] or visited[nx][ny]:
#                     continue
#                 visited[nx][ny] = visited[x][y] + 1
#                 queue.append([nx, ny])
#         else:
#             for ix, iy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
#                 nx = x + ix
#                 ny = y + iy
#                 if nx < 0 or nx >= h or ny < 0 or ny >= w:
#                     continue
#                 if graph[nx][ny] or visited[nx][ny]:
#                     continue
#                 visited[nx][ny] = visited[x][y] + 1
#                 queue.append([nx, ny])
#     return -1
# print(bfs())
from collections import deque

k = int(input())
w, h = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]
visited = [[[0]*w for _ in range(h)] for _ in range(k+1)]
h_dist = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
m_dist = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def bfs():
    queue = deque()
    queue.append([0, 0, 0])
    visited[0][0][0] = 1
    while queue:
        z, x, y = queue.popleft()
        if x == h-1 and y == w-1:
            return visited[z][x][y] - 1

        for dx, dy in m_dist:
            nx = x + dx
            ny = y + dy
            if nx < 0 or nx >= h or ny < 0 or ny >= w:
                continue
            if visited[z][nx][ny] or graph[nx][ny]:
                continue
            visited[z][nx][ny] = visited[z][x][y] + 1
            queue.append([z, nx, ny])

        if z < k:
            for ix, iy in h_dist:
                hx = x + ix
                hy = y + iy
                if hx < 0 or hx >= h or hy < 0 or hy >= w:
                    continue
                if graph[hx][hy] or visited[z+1][hx][hy]:
                    continue
                visited[z+1][hx][hy] = visited[z][x][y] + 1
                queue.append([z+1, hx, hy])
    return -1


print(bfs())