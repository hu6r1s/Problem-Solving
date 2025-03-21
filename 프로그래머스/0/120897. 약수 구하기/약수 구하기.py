def solution(n):
    return sorted(set(sum([[i, n // i] for i in range(1, int(n ** 0.5)+1) if not n % i], [])))