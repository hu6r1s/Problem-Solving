from collections import defaultdict

def solution(arr, queries):
    cnt = defaultdict(int)
    
    for query in queries:
        for i in range(query[0], query[1]+1):
            arr[i] += 1
    # for name, value in cnt.items():
    #     arr[name] += value
    return arr