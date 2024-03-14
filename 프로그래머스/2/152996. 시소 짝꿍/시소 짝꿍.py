from itertools import product, combinations, combinations_with_replacement

def solution(weights):
    count = 0
    dict1 = dict()
    for weight in weights:
        dict1[weight] = dict1.get(weight, 0) + 1
    for weight in weights:
        if weight % 2 == 0:
            count += dict1.get(weight*3//2, 0)
        if weight % 3 == 0:
            count += dict1.get(weight*4//3, 0)
        count += dict1.get(weight*2, 0)
    for weight in weights:
        dict1[weight] -= 1
        count += dict1[weight]
    return count