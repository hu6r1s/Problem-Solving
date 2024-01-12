def solution(answers):
    a1 = [1, 2, 3, 4, 5]
    a2 = [2, 1, 2, 3, 2, 4, 2, 5]
    a3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    c1, c2, c3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == a1[i%len(a1)]:
            c1 += 1
        if answers[i] == a2[i%len(a2)]:
            c2 += 1
        if answers[i] == a3[i%len(a3)]:
            c3 += 1
    result = []
    chk = max(c1, c2, c3)
    if c1 == chk:
        result.append(1)
    if c2 == chk:
        result.append(2)
    if c3 == chk:
        result.append(3)
    return result