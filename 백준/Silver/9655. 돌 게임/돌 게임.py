n = int(input())
dp = ["" for _ in range(n+1)]
dp[1] = "SK"
for i in range(2, n+1):
    if dp[i-1] == "SK":
        dp[i] = "CY"
    else:
        dp[i] = "SK"
print(dp[-1])