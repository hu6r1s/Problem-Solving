def solution(x):
    s = list(map(int, str(x)))
    if x % sum(s) == 0:
        return True
    else:
        return False