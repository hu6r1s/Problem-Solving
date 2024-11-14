from collections import deque


n = int(input())
graph = [[i for i in map(int, input().split())] for _ in range(n)]
#
# for k in range(n):
#     for i in range(n):
#         for j in range(n):
#             if graph[i][k] and graph[k][j]:
#                 graph[i][j] = 1
#
# for g in graph:
#     print(*g)

visited = [[False] * n for _ in range(n)]


def bfs(x):
    queue = deque([x])
    check = [False for _ in range(n)]
    while queue:
        v = queue.popleft()
        for i in range(n):
            if not check[i] and graph[v][i]:
                queue.append(i)
                check[i] = True
                graph[x][i] = 1


for i in range(n):
    bfs(i)

for g in graph:
    print(*g)