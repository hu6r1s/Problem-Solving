from collections import deque
import sys
input = sys.stdin.readline
queue = deque()

n = int(input())
for _ in range(n):
    cmd = input().split()
    if cmd[0] == "push":
        queue.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        if queue:
            print(0)
        else:
            print(1)
    elif cmd[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif cmd[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)