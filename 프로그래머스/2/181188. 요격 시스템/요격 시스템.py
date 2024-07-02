def solution(targets):
    targets.sort(key=lambda x: x[1])
    cur = 0
    result = 0
    for target in targets:
        if cur > target[0]: continue
        cur = target[1]
        result += 1
    return result