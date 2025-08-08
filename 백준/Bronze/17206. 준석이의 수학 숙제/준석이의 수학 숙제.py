dp = [0] * 80001
dp[1] = 1
cnt = 0
for i in range(2, 80001):
    if not i % 3 or not i % 7:
        cnt += i
    dp[i] = cnt

t = int(input())
n = list(map(int, input().split()))
for i in n:
    print(dp[i])