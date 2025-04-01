import copy

def solution(arr):
    count = 0
    while True:
        cur_arr = copy.copy(arr)
            
        for i in range(len(arr)):
            if 50 <= arr[i] and not arr[i] % 2:
                arr[i] = arr[i] // 2
            elif 50 > arr[i] and arr[i] % 2:
                arr[i] = arr[i] * 2 + 1
        
        if cur_arr == arr:
            break
        
        count += 1
    return count
    