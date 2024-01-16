import sys
input = sys.stdin.readline

n = int(input())
count = 0
for _ in range(n):
    string = input().rstrip()
    stack = []
    for s in string:
        if stack and stack[-1] == s:
            stack.pop()
        else:
            stack.append(s)
    else:
        if not stack:
            count += 1
print(count)