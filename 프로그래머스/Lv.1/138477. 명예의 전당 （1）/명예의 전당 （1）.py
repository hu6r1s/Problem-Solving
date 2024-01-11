def solution(k, score):
    result = []
    tmp = []
    for s in score:
        if len(tmp) != k:
            tmp.append(s)
            tmp.sort(reverse=True)
            result.append(tmp[-1])
        else:
            if s > tmp[-1]:
                tmp.insert(0, s)
                tmp.pop()
                tmp.sort(reverse=True)
                result.append(tmp[-1])
            else:
                result.append(tmp[-1])
    return result