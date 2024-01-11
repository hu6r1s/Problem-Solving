def solution(k, score):
    result = []
    tmp = []
    for s in score:
        if len(tmp) < k:
            tmp.append(s)
            result.append(min(tmp))
            tmp.sort(reverse=True)
        else:
            tmp.sort(reverse=True)
            if s > tmp[-1]:
                tmp.insert(0, s)
                tmp.pop()
                result.append(min(tmp))
            else:
                result.append(min(tmp))
    return result