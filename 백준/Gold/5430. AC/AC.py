import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = list(input().rstrip())
    n = int(input())
    queue = deque(input().rstrip()[1:-1].split(","))
    count = 0
    if n == 0:
        queue = []
    for i in p:
        if i == "R":
            count += 1
        elif i == "D":
            if queue:
                if count % 2 == 0:
                    queue.popleft()
                else:
                    queue.pop()
            else:
                print("error")
                break
    else:
        if count % 2 == 0:
            print("["+",".join(queue)+"]")
        else:
            queue.reverse()
            print("["+",".join(queue)+"]")