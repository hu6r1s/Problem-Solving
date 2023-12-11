import sys
input = sys.stdin.readline

n = int(input())
li = [int(input()) for _ in range(n)]
for i in sorted(li):
    print(i)