def solution(arr):
    for i in range(len(arr)):
        arr[i].extend([0] * (len(arr) - len(arr[i])))
    
    for _ in range(len(arr), len(arr[0])):
        arr.append([0] * len(arr[0]))
    
    return arr