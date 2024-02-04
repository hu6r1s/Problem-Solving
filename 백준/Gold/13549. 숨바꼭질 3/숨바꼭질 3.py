from collections import deque


n, k = map(int, input().split())
graph = [0 for _ in range(100001)]

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if x == k:
            return graph[x]
        for nx in (2*x, x-1, x+1):
            if nx < 0 or nx >= 100001:
                continue
            if graph[nx]:
                continue
            if nx == 2 * x:
                graph[nx] = graph[x]
                queue.append(nx)
            else:
                graph[nx] = graph[x] + 1
                queue.append(nx)


print(bfs())