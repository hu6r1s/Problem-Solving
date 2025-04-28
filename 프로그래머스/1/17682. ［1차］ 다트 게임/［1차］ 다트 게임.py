def solution(dartResult):
    tmp = ''
    scores = []
    for dart in dartResult:
        if dart.isdigit():
            tmp += dart
        if dart in 'SDT':
            num = int(tmp)
            if dart == 'S':
                num = num ** 1
            elif dart == 'D':
                num = num ** 2
            elif dart == 'T':
                num = num ** 3

            scores.append(num)
            tmp = ''
        if dart == '*':
            if len(scores) >= 2:
                scores[-2] *= 2
            scores[-1] *= 2
        elif dart == '#':
            scores[-1] *= -1
        
    return sum(scores)