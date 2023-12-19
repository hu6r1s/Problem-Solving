import math
import sys
input = sys.stdin.readline

def prime(x):
    arr = [False, False] + [True] * (x-1)
    for i in range(2, int(math.sqrt(x))+1):
        if arr[i]:
            for j in range(2*i, x+1, i):
                arr[j] = False
    return arr

while True:
    n = int(input())
    if n == 0:
        break
    arr = prime(2*n)
    print(arr[n+1:].count(True))