def solution(survey, choices):
    type = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}
    score = {1: 3, 2: 2, 3: 1, 4: 0, 5: 1, 6: 2, 7: 3}
    result = ""
    for i in range(len(survey)):
        if choices[i] <= 4:
            type[survey[i][0]] += score[choices[i]]
        else:
            type[survey[i][1]] += score[choices[i]]
            
    type_key = list(type.keys())
    for i in range(0, len(type_key), 2):
        if type[type_key[i]] >= type[type_key[i+1]]:
            result += type_key[i]
        else:
            result += type_key[i+1]
    return result