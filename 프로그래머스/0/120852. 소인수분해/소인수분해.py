def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True

def solution(n):
    result = []
    for i in range(2, n+1):
        if not n % i and is_prime(i):
            result.append(i)
    return result