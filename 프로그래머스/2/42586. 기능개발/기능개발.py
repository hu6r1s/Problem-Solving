def solution(progresses, speeds):
    result = []
    while progresses:
        count = 0
        while progresses and progresses[0] >= 100:
            count += 1
            progresses.pop(0)
            speeds.pop(0)
        
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        if count:
            result.append(count)
    return result