def solution(n):
    result = 0
    
    while n > 0:
        if not n % 2:
            n //= 2
        else:
            n -= 1
            result += 1
    return result