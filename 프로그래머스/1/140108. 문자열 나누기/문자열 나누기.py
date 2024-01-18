def solution(s):
    count1 = 0
    count2 = 0
    result = 0
    for i in s:
        if count1 == count2:
            result += 1
            c = i
        if c == i:
            count1 += 1
        else:
            count2 += 1
    return result