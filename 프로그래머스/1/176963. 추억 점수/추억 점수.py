def solution(name, yearning, photo):
    miss = dict.fromkeys(name)
    for i in range(len(yearning)):
        miss[name[i]] = yearning[i]
    
    result = []
    for p in photo:
        point = 0
        for n in p:
            if n not in miss.keys():
                continue
            point += miss[n]
        result.append(point)
    return result