n = int(input())
dp = [False if i ** 0.5 % 1 else True for i in range(n+1)]

num = 4
for i in range(int(n**0.5), 0, -1):
    if dp[n]:
        num = 1
        break
    elif dp[n-i**2]:
        num = 2
        break
    else:
        for j in range(int((n-i**2)**0.5), 0, -1):
            if dp[(n-i**2)-j**2]:
                num = 3
                break
print(num)