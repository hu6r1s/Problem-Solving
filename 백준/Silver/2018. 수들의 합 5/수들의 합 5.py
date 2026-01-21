n = int(input())
start, end = 1, 1
sum_num, cnt = 1, 1

# while end < n:
#     if sum_num == n:
#         cnt += 1
#         end += 1
#         sum_num += end
#     elif sum_num < n:
#         end += 1
#         sum_num += end
#     else:
#         sum_num -= start
#         start += 1
#
# print(cnt)

while end < n:
    if sum_num == n:
        cnt += 1
        start += 1
        end = start + 1
        sum_num = start + end
    elif sum_num < n:
        end += 1
        sum_num += end
    else:
        sum_num -= start
        start += 1

print(cnt)

"""
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
s
        e
"""