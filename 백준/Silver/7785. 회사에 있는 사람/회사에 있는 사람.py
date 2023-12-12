import sys
input = sys.stdin.readline

n = int(input())
li = dict()
for _ in range(n):
    human, log = input().split()
    if log == "enter":
        li[human] = log
    else:
        del li[human]
for i in sorted(li.keys(), reverse=True):
    print(i)