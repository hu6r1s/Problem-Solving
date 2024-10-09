from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
queue = deque()
for _ in range(n):
    lst = input().split()

    if lst[0] == "push":
        queue.append(int(lst[1]))
    elif lst[0] == "pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif lst[0] == "size":
        print(len(queue))
    elif lst[0] == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif lst[0] == "front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif lst[0] == "back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])