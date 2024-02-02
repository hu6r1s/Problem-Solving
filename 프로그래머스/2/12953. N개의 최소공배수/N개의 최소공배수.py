import math

def solution(arr):
    def lcm(x, y):
        return x * y // math.gcd(x, y)
    result = []
    while True:
        arr.append(lcm(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]