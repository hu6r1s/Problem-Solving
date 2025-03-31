def solution(strArr):
    arr = [len(s) for s in strArr]
    set_arr = set(arr)
    result = []
    for a in set_arr:
        result.append(arr.count(a))
    return max(result)