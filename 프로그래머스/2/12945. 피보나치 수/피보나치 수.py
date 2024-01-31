
def solution(n):
    pre = 0
    cur = 1
    for _ in range(2, n+1):
        pre, cur = cur, pre + cur
    return cur % 1234567
