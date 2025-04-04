def solution(score):
    avg = [(en + math) / 2 for en, math in score]
    sort_avg = sorted(avg, reverse=True)
    return [sort_avg.index(i) + 1 for i in avg]