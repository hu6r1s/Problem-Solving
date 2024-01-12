def solution(n, m, section):
    count = 0
    while section:
        left = section[0]
        right = left + m
        while section and section[0] < right:
            section.pop(0)
        count += 1
    return count