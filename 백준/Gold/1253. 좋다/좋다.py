import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
a.sort()
cnt = 0

# for i in a[2:]:
#     start = a[0]
#     end = a[1]
#     while start + end <= i:
#         if start + end == i:
#             cnt += 1
#             break
#         elif start + end < i:
#             end += 1
#         else:
#             start += 1
# print(cnt)

for i in range(n):
    start = 0
    end = n - 1
    target = a[i]
    while start < end:
        if a[start] + a[end] == target:
            if start != i and end != i:
                cnt += 1
                break
            elif start == i:
                start += 1
            elif end == i:
                end -= 1
        elif a[start] + a[end] < target:
            start += 1
        else:
            end -= 1
print(cnt)

"""
1 2 3 4 5 6 7 8 9 10
s
  e
"""