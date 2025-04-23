import heapq

def solution(operations):
    max_heap = []
    min_heap = []
    visited = [False] * len(operations)
    for idx, op in enumerate(operations):
        cmd, n = op.split()
        if cmd == "I":
            heapq.heappush(max_heap, (-int(n), idx))
            heapq.heappush(min_heap, (int(n), idx))
        elif cmd == "D" and int(n) == 1:
            while max_heap and visited[max_heap[0][1]]:
                heapq.heappop(max_heap)
            if max_heap:
                _, key = heapq.heappop(max_heap)
                visited[key] = True
        elif cmd == "D" and int(n) == -1:
            while min_heap and visited[min_heap[0][1]]:
                heapq.heappop(min_heap)
            if min_heap:
                _, key = heapq.heappop(min_heap)
                visited[key] = True
                
    while min_heap and visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    if not max_heap:
        return [0, 0]
    else:
        return [-max_heap[0][0], min_heap[0][0]]