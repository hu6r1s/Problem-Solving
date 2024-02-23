n = int(input())
s = [0]+[int(input()) for _ in range(n)]
dp = [[0]*3 for _ in range(n+1)]
dp[0][0], dp[0][1], dp[0][2] = 0, 0, 0
for i in range(1, n+1):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2])
    dp[i][1] = dp[i-1][0] + s[i]
    dp[i][2] = dp[i-1][1] + s[i]

print(max(dp[n][1], dp[n][2]))