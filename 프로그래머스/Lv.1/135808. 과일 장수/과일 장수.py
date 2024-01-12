def solution(k, m, score):
    score.sort(reverse=True)
    count = 0
    for i in range(0, len(score), m):
        tmp = score[i:i+m]
        if len(tmp) == m:
            count += min(tmp) * m
    return count