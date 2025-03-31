import math

def solution(n):
    result = 10
    while result >= 0:
        if n < math.factorial(result):
            result -= 1
        else:
            break
    return result