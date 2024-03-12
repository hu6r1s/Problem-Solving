def solution(clothes):
    dict1 = dict()
    for cloth, type in clothes:
        if type in dict1:
            dict1[type] += 1
        else:
            dict1[type] = 1
    count = 1
    for i in dict1.values():
        count *= i+1
    return count-1