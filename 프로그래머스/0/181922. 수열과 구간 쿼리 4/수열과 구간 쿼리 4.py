def solution(arr, queries):
    for query in queries:
        for i in range(query[0], query[1]+1):
            if not i % query[2]:
                arr[i] += 1
    return arr