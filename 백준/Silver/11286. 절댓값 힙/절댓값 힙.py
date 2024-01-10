import heapq
import sys
input = sys.stdin.readline

n = int(input())
result = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if not result:
            print(0)
        else:
            print(heapq.heappop(result)[1])
    else:
        heapq.heappush(result, (abs(x), x))