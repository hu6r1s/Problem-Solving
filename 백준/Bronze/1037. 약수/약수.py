import sys
import math
input = sys.stdin.readline

n = int(input())
m = sorted(list(map(int, input().split())))
print(m[0] * m[-1])