def solution(arr, k):
    result = []
    for i in range(len(arr)):
        if arr[i] in result:
            continue
        result.append(arr[i])
    return result[:k] if len(result) >= k else result + [-1] * (k - len(result))