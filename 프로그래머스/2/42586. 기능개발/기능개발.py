from collections import deque

def solution(progresses, speeds):
    days = deque()
    for i in range(len(progresses)):
        count = 0
        while progresses[i] < 100:
            progresses[i] += speeds[i]
            count += 1
        days.append(count)
    
    result = []
    while days:
        day = days.popleft()
        a = 1
        while days and day >= days[0]:
            a += 1
            days.popleft()
        
        result.append(a)
        
    return result