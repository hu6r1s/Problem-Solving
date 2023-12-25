import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
queue = deque(enumerate(map(int, input().split())))
result = []
while queue:
    index, init = queue.popleft()
    result.append(index + 1)
    if init > 0:
        queue.rotate(-(init-1))
    elif init < 0:
        queue.rotate(-init)
print(" ".join(map(str, result)))