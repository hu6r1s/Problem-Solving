from itertools import combinations
import math
    
def isPrime(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
def solution(nums):
    chk = []
    count = 0
    for c in combinations(nums, 3):
        chk.append(sum(c))
    for i in chk:
        if isPrime(i):
            count += 1

    return count