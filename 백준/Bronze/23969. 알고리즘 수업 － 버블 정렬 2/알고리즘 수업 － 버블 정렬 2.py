n, k = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

for i in range(n-1, 0, -1):
    for j in range(i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
            cnt += 1

            if cnt == k:
                print(*nums)
                exit(0)

print(-1)