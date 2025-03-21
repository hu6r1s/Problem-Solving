def solution(d, budget):
    d.sort()
    result = 0
    total = 0
    for cost in d:
        total += cost
        if total > budget:
            break
        result += 1
    return result