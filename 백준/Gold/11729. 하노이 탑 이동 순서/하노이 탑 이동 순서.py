import sys
import math
input = sys.stdin.readline

def hanoi(n, start, end, sub):
    if n == 1:
        move(start, end)
        return
    hanoi(n-1, start, sub, end)
    move(start, end)
    hanoi(n-1, sub, end, start)

def move(start, end):
    print(start, end)

n = int(input())
print(2**n - 1)
hanoi(n, 1, 3, 2)