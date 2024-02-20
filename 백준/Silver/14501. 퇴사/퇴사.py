n = int(input())
arr = [0] * n
price = [0] * n
dp = [0] * (n+1)

for i in range(n):
    arr[i], price[i] = map(int, input().split())

for i in range(n-1, -1, -1):
    if i + arr[i] <= n:
        dp[i] = max(dp[i+arr[i]]+price[i], dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])