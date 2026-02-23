from collections import deque

n = int(input())
trees = [[] for _ in range(n+1)]
for _ in range(n):
    data = list(map(int, input().split()))
    v = data[0]

    idx = 1
    while data[idx] != -1:
        to = data[idx]
        dist = data[idx+1]
        trees[v].append((to, dist))
        idx += 2

distance = [0] * (n+1)

def bfs(v):
    queue = deque()
    queue.append((v, 0))
    visited = [False] * (n+1)
    visited[v] = True
    far_node = v
    far_dist = 0

    while queue:
        x, dist = queue.popleft()
        if dist > far_dist:
            far_dist = dist
            far_node = x

        for tree in trees[x]:
            if not visited[tree[0]]:
                visited[tree[0]] = True
                queue.append((tree[0], dist + tree[1]))
    return far_node, far_dist


nodeA, _ = bfs(1)
_, result = bfs(nodeA)
print(result)