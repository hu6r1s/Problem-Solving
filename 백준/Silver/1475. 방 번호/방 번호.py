n = input()
dp = [0] * 10
for i in n:
    if int(i) == 6 or int(i) == 9:
        if dp[6] < dp[9]:
            dp[6] += 1
        else:
            dp[9] += 1
    else:
        dp[int(i)] += 1
print(max(dp))