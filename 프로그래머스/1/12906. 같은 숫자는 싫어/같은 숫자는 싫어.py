def solution(arr):
    stack = [arr[0]]
    for i in range(len(arr)-1):
        if arr[i+1] != arr[i]:
            stack.append(arr[i+1])
    return stack