from itertools import combinations

def solution(number):
    result = 0
    for c in combinations(number, 3):
        if sum(c) == 0:
            result += 1
    return result