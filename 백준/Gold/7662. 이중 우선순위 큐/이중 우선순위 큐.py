import heapq
from collections import defaultdict
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    k = int(input())
    max_heap = []
    min_heap = []
    valid = defaultdict(int)

    for _ in range(k):
        s, n = input().split()
        n = int(n)
        if s == "I":
            heapq.heappush(max_heap, -n)
            heapq.heappush(min_heap, n)
            valid[n] += 1
        elif s == "D":
            if n == 1:
                while max_heap and valid[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    v = -heapq.heappop(max_heap)
                    valid[v] -= 1
            elif n == -1:
                while min_heap and valid[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    v = heapq.heappop(min_heap)
                    valid[v] -= 1

    while max_heap and valid[-max_heap[0]] == 0:
        heapq.heappop(max_heap)
    while min_heap and valid[min_heap[0]] == 0:
        heapq.heappop(min_heap)

    print(f"{-max_heap[0]} {min_heap[0]}" if max_heap and min_heap else "EMPTY")