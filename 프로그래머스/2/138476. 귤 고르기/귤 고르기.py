def solution(k, tangerine):
    t = dict()
    count = 0
    for i in tangerine:
        if i in t:
            t[i] += 1
        else:
            t[i] = 1
    t = dict(sorted(t.items(), key=lambda x: x[1], reverse=True))
    for i in t:
        if k <= 0:
            return count
        k -= t[i]
        count += 1
    return count