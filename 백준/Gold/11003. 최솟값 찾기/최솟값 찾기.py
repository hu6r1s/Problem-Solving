from collections import deque

n, l = map(int, input().split())
queue = deque()
a = list(map(int, input().split()))

for i in range(n):
    while queue and queue[-1][1] > a[i]:
        queue.pop()
    queue.append((i, a[i]))
    if queue[0][0] <= i - l:
        queue.popleft()
    print(queue[0][1], end=" ")