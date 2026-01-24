# n, l = map(int, input().split())
# a = list(map(int, input().split()))
# min_num = []
#
# idx = 0
# while idx < n:
#     if idx - l + 1 < 0:
#         min_num.append(min(a[:idx+1]))
#     else:
#         min_num.append(min(a[idx - l + 1: idx+1]))
#     idx += 1
#
# print(*min_num)

from collections import deque

n, l = map(int, input().split())
a = list(map(int, input().split()))
queue = deque()
result = []

for i in range(n):
    while queue and queue[-1][1] > a[i]:
        queue.pop()
    queue.append([i, a[i]])
    if queue[0][0] <= i - l:
        queue.popleft()
    result.append(queue[0][1])
    
print(*result)

"""
1 5 2 3 6 2 3 7 3 5 2 6

d(1) = a(-1) ~ a(1)
d(2) = a(0) ~ a(2)
d(3) = a(1) ~ a(3)
"""