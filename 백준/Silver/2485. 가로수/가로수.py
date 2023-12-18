import math
import sys
input = sys.stdin.readline

n = int(input())
garosu = [int(input()) for _ in range(n)]
gaps = []
for i in range(n-1, 0, -1):
    gaps.append(garosu[i]-garosu[i-1])
g = garosu[1] - garosu[0]
for gap in gaps:
    g = math.gcd(gap, g)

result = 0
for gap in gaps:
    result += gap // g - 1
print(result)