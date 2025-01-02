def solution(numbers):
    return str(int("".join(map(str, sorted(numbers, key=lambda x: str(x)*4, reverse=True)))))