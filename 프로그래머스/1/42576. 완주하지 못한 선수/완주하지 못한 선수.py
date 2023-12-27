def solution(participant, completion):
    dict1 = dict()
    for i in participant:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    for i in completion:
        dict1[i] -= 1
    for i in dict1.keys():
        if dict1[i] != 0:
            return i