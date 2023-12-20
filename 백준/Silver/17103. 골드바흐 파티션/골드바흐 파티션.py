import math
import sys
input = sys.stdin.readline

t = int(input())
arr = [False, False] + [True] * (999999)
for i in range(2, int(math.sqrt(1000000))+1):
    if arr[i]:
        for j in range(2*i, 1000001, i):
            arr[j] = False

for _ in range(t):
    n = int(input())

    count = 0
    for i in range(2, n//2+1):
        if arr[i] and arr[n-i]:
            count += 1
    print(count)