import sys
import math
input = sys.stdin.readline

def kantour(n):
    if n == 1:
        return "-"

    left = kantour(n//3)
    center = " " * (n//3)
    return left + center + left

while True:
    try:
        n = int(input())
        print(kantour(3**n))
    except:
        break