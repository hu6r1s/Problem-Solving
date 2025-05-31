def solution(n, times):
    start = 1
    end = n * max(times)
    result = 0
    while start <= end:
        mid = (start + end) // 2
        cnt = 0
        for time in times:
            cnt += mid // time
        if cnt >= n:
            result = mid
            end = mid - 1
        else:
            start = mid + 1
    return result