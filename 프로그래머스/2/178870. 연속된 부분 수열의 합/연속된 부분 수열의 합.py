def solution(sequence, k):
    result = []
    s = 0
    i, j = -1, 0
    while True:
        if s < k:
            i += 1
            if i >= len(sequence):
                break
            s += sequence[i]
        else:
            s -= sequence[j]
            if j >= len(sequence):
                break
            j += 1
        if s == k:
            result.append([j, i])
    result.sort(key=lambda x: (x[1]-x[0], x[0]))
    return result[0]