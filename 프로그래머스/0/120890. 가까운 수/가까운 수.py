def solution(array, n):
    array.sort(key=lambda x: (abs(n-x), x))
    return array[0]