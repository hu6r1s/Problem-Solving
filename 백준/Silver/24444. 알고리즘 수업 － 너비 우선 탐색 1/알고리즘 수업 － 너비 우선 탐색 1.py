from collections import deque
import sys
input = sys.stdin.readline

def bfs(graph, visited, r):
    global count
    visited[r] = count
    queue = deque([r])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                count += 1
                visited[i] = count

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
count = 1
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for g in graph:
    g.sort()

bfs(graph, visited, r)
for v in visited[1:]:
    print(v)