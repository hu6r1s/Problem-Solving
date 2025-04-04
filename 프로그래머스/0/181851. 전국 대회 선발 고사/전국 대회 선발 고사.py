def solution(rank, attendance):
    rank = list(sorted(enumerate(rank), key=lambda x: x[1]))
    result = []
    for idx, value in rank:
        if len(result) == 3:
            break
        if attendance[idx]:
            result.append(idx)
    return 10000 * result[0] + 100 * result[1] + result[2]