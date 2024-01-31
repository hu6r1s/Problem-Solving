def solution(s):
    num = list(map(int, s.split()))
    return "{} {}".format(min(num), max(num))