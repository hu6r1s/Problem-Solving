import math

def solution(n):
    x = math.sqrt(n)
    if int(x) == x:
        return math.pow(x+1, 2)
    else:
        return -1