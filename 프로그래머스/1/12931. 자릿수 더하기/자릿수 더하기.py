def solution(n):
    li = list(str(n))
    result = 0
    for i in li:
        result += int(i)
    return result