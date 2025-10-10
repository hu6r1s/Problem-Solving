from collections import deque

def solution(cacheSize, cities):
    cache = deque(maxlen=cacheSize)
    cnt = 0
        
    for i in range(len(cities)):
        cities[i] = cities[i].lower()
        if cities[i] in cache:
            cache.remove(cities[i])
            cache.append(cities[i])
            cnt += 1
        else:
            cache.append(cities[i])
            cnt += 5
    return cnt
    
    
    
"""
[, , , , , seoul, jeju, pangyo]
5 + 5 + 5 + 1 + 1 + 1 + 1 + 1 + 1
"""