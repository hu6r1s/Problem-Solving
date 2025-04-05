from collections import deque

def solution(A, B):
    A = deque(A)
    result = 0
    while True:
        if "".join(A) == B:
            return result
        if result == len(A):
            return -1
        A.rotate(1)
        result += 1
    