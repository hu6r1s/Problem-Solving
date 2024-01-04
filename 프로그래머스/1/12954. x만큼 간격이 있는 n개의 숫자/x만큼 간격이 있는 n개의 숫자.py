def solution(x, n):
    result = []
    i = 1
    while True:
        if len(result) == n:
            break
        result.append(x * i)
        i += 1
    return result