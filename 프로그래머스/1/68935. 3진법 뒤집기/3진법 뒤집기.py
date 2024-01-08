def solution(n):
    s = ""
    while n:
        s += str(n % 3)
        n //= 3
    s = list(reversed(s))
    result = 0
    for i in range(len(s)):
        result += int(s[i]) * 3 ** i
    return result