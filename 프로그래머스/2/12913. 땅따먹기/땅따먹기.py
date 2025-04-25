def solution(land):
    dp = [[0] * 4 for _ in range(len(land))]
    dp[0] = land[0]
    
    for i in range(1, len(land)):
        for j in range(4):
            dp[i][j] = max(dp[i-1][k] + land[i][j] for k in range(4) if j != k)
    return max(dp[-1])
    
# dp로 풀이
# 1로 갔을 때 1 + 6, 1 + 7, 1 + 8 
# 2로 갔을 때 2 + 5, 2 + 7, 2 + 8 
# 3로 갔을 때 3 + 5, 3 + 6, 3 + 8 
# 5로 갔을 때 
