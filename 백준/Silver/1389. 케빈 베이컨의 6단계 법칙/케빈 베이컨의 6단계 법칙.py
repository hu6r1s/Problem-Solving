from collections import deque


def bfs(relation, s):
    queue = deque([s])
    cnt = [0] * (n+1)
    visited[s] = True
    while queue:
        new = queue.popleft()
        for i in relation[new]:
            if not visited[i]:
                cnt[i] = cnt[new] + 1
                visited[i] = True
                queue.append(i)
    return sum(cnt)


n, m = map(int, input().split())
relation = [[] for _ in range(n+1)]
result = [0]

for _ in range(m):
    a, b = map(int, input().split())
    relation[a].append(b)
    relation[b].append(a)

for i in range(1, n+1):
    visited = [False] * (n+1)
    result.append(bfs(relation, i))

print(result.index(min(result[1:])))