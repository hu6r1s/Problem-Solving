n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())
cnt = 0
start, end = 0, n - 1

while start < end:
    if nums[start] + nums[end] == x:
        cnt += 1
        start += 1
    elif nums[start] + nums[end] < x:
        start += 1
    else:
        end -= 1

print(cnt)