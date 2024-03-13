import heapq

def solution(n, k, enemy):
    heap = []
    sumEnemy = 0
    result = 0
    for e in enemy:
        heapq.heappush(heap, -e)
        sumEnemy += e
        
        if sumEnemy > n:
            if k == 0:
                break
            sumEnemy += heapq.heappop(heap)
            k -= 1
        result += 1
    return result