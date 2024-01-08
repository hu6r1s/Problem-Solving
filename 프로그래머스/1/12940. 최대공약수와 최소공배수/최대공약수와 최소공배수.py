def solution(n, m):
    result = []
    a, b = m, n
    while a % b != 0:
        a, b = b, a % b
    result.append(b)
    result.append(m*n//b)
    return result