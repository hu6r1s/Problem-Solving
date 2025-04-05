def solution(n):
    count = 0
    num = 0
    while count < n:
        num += 1
        if not num % 3 or '3' in str(num):
            continue
        count += 1
    return num