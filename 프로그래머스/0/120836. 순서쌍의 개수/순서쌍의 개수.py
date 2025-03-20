def solution(n):
    result = 0
    i = 1
    while True:
        if i == n:
            result += 1
            break
        if not n % i:
            result += 1
        i += 1
    return result