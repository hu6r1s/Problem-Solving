def solution(arr, queries):
    result = []
    for s, e, k in queries:
        a = [i for i in arr[s:e+1] if i > k]
        if a:
            result.append(min(a))
        else:
            result.append(-1)
    return result