import sys
import math
input = sys.stdin.readline

def fibo(x):
    if x <= 1:
        return x
    return fibo(x-1) + fibo(x-2)
print(fibo(int(input())))