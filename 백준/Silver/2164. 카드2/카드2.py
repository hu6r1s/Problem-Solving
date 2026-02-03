from collections import deque
import sys
input = sys.stdin.readline
queue = deque()

n = int(input())
for i in range(1, n+1):
    queue.append(i)
while len(queue) != 1:
    queue.popleft()
    queue.append(queue.popleft())
print(*queue)