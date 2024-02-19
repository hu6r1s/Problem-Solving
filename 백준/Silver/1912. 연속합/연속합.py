n = int(input())
arr = [0] + list(map(int, input().split()))
dp = [0] * (n+1)
dp[1] = arr[1]

if max(arr) > 0:
    for i in range(1, n+1):
        dp[i] = max(0, dp[i-1] + arr[i])
    print(max(dp))
else:
    print(max(arr[1:]))