def solution(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b % 1234567