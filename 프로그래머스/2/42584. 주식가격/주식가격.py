from collections import deque
def solution(prices):
    queue = deque(prices)
    result = []
    
    while queue:
        q = queue.popleft()
        count = 0
        for i in queue:
            count += 1
            if q > i:
                break
        result.append(count)
    return result