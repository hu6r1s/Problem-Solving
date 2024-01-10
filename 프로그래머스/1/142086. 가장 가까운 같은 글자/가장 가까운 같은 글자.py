def solution(s):
    check = {}
    result = []
    for i in range(len(s)):
        if s[i] not in check.keys():
            result.append(-1)
        else:
            result.append(i-check[s[i]])
        check[s[i]] = i
    return result