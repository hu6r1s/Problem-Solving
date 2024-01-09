def solution(t, p):
    li = []
    result = 0
    for i in range(0, len(t)):
        li.append(t[i:i+len(p)])
    for i in li:
        if len(i) == len(p):
            if i <= p:
                result += 1
    return result