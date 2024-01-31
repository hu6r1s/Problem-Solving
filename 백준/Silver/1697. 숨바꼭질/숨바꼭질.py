from collections import deque

n, k = map(int, input().split())
dist = [0]*100001

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        q = queue.popleft()
        if q == k:
            return dist[q]
        for nq in (q-1, q+1, q*2):
            if 0 <= nq <= 100000 and not dist[nq]:
                dist[nq] = dist[q] + 1
                queue.append(nq)

print(bfs())