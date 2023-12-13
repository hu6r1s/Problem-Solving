import sys
input = sys.stdin.readline

n = int(input())
sugn = set(map(int, input().split()))
m = int(input())
a = list(map(int, input().split()))
for i in a:
    if i in sugn:
        print(1, end=" ")
    else:
        print(0, end=" ")