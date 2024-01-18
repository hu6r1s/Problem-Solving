def solution(keymap, targets):
    result = []
    match = dict()
    for key in keymap:
        for idx, value in enumerate(key):
            if value in match.keys():
                if idx + 1 < match[value]:
                    match[value] = idx + 1
            else:
                match[value] = idx + 1
    
    for target in targets:
        count = 0
        for t in target:
            if t in match.keys():
                count += match[t]
            else:
                count = -1
                break
        result.append(count)
    return result