from collections import deque

def solution(numbers, k):
    arr = deque(numbers)
    arr.rotate(-(2 * (k - 1)))
    return arr[0]
    