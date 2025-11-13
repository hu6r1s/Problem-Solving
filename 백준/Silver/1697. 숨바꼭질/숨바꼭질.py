from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001

def bfs():
    queue = deque()
    queue.append(n)
    cnt = 0
    while queue:
        x = queue.popleft()
        if x == k:
            return visited[k]
        for nx in [x-1, x+1, 2*x]:
            if nx > 100000 or nx < 0 or visited[nx] != 0:
                continue
            visited[nx] = visited[x] + 1
            queue.append(nx)

print(bfs())