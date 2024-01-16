def solution(X, Y):
    chk = set(X) & set(Y)
    if not chk:
        return "-1"
    else:
        if len(chk) == 1 and "0" in chk:
            return "0"
        result = [i * min(X.count(i), Y.count(i)) for i in chk]
        return "".join(sorted(result, reverse=True))