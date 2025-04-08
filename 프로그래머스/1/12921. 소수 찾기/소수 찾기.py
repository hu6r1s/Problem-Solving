def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def solution(n):
    result = 0
    for i in range(2, n+1):
        if is_prime(i):
            result += 1
    return result