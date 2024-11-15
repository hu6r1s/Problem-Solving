from collections import deque


n, m = map(int, input().split())
ladder, snake = dict(), dict()

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    u, v = map(int, input().split())
    snake[u] = v

visited = [False] * 101


def bfs(x):
    queue = deque([x])
    visited[x] = True
    count = 0
    while queue:
        l = len(queue)
        for _ in range(l):
            v = queue.popleft()
            if v == 100:
                return count
            for i in range(1, 7):
                nv = v + i
                if nv > 100 or visited[nv]:
                    continue
                if nv in ladder.keys():
                    queue.append(ladder[nv])
                    visited[ladder[nv]] = True
                elif nv in snake.keys():
                    queue.append(snake[nv])
                    visited[snake[nv]] = True
                else:
                    queue.append(nv)
                    visited[nv] = True
        count += 1


print(bfs(1))