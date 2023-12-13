import sys
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    a2, b2 = a, b
    while a2 % b2 != 0:
        a2, b2 = b2, a2 % b2
    print(a*b// b2)