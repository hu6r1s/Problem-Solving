import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
queue = deque([i for i in range(1, n+1)])
x = list(map(int, input().split()))
count = 0
for i in range(m):
    while True:
        if x[i] == queue[0]:
            queue.popleft()
            break
        else:
            if queue.index(x[i]) <= len(queue)//2:
                queue.append(queue.popleft())
            else:
                queue.appendleft(queue.pop())
            count += 1
print(count)