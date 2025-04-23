def solution(triangle):
    cnt = [[0] * len(t) for t in triangle]
    cnt[0][0] = triangle[0][0]
    for t in range(1, len(triangle)):
        for i in range(len(triangle[t])):
            if i == 0: 
                cnt[t][i] = cnt[t-1][i] + triangle[t][i]
            elif i == len(triangle[t]) - 1:
                cnt[t][i] = cnt[t-1][i-1] + triangle[t][i]
            else:
                cnt[t][i] = max(cnt[t-1][i-1] + triangle[t][i], cnt[t-1][i] + triangle[t][i])
    return max(cnt[-1])
# cnt[0][0] = triangle[0][0]
# cnt[1][0] = cnt[0][0] + triangle[1][0]
# cnt[1][1] = cnt[0][0] + triangle[1][1]
# cnt[2][0] = cnt[1][0] + triangle[1][0]
# cnt[2][1] = max(cnt[1][0] + triangle[2][1], cnt[1][1] + triangle[2][1])
# cnt[2][2] = cnt[1][1] + triangle[2][2]