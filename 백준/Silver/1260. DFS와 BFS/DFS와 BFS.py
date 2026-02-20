import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

graph = [sorted(g) for g in graph]

visited = [False] * (n+1)


def dfs(v):
    visited[v] = True
    print(v, end=" ")

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


dfs(v)
visited = [False] * (n+1)


def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        x = queue.popleft()
        print(x, end=" ")
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


print()
bfs(v)