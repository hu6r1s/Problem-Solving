def solution(n, arr1, arr2):
    arr = []
    for i in range(n):
        arr.append(bin(arr1[i] | arr2[i])[2:].zfill(n))
        
    for i in range(n):
        arr[i] = arr[i].replace("1", "#").replace("0", " ")
    return arr