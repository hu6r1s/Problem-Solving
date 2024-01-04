def solution(n):
    li = list(map(int, str(n)))
    return int("".join(map(str, sorted(li, reverse=True))))