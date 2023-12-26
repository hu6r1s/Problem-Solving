import sys
import math
input = sys.stdin.readline

def factorail(x):
    if x == 0:
        return 1
    return x * factorail(x-1)
print(factorail(int(input())))