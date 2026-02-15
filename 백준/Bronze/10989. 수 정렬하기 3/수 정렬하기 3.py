import sys
input = sys.stdin.readline

n = int(input())
s = [0] * 10001
for _ in range(n):
    s[int(input())] += 1

for i in range(10001):
    while s[i]:
        print(i)
        s[i] -= 1