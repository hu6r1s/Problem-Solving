def solution(clothes):
    dict1 = dict()
    for i, j in clothes:
        if j in dict1:
            dict1[j] += 1
        else:
            dict1[j] = 1
    count = 1
    for i in dict1.values():
        count *= i + 1
    return count - 1