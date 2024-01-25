def solution(today, terms, privacies):
    term = dict()
    today = list(map(int, today.split(".")))
    result = []
    for t in terms:
        tmp = t.split()
        term[tmp[0]] = int(tmp[1])
        
    for i in range(len(privacies)):
        privacy = privacies[i].split(" ")
        days = list(map(int, privacy[0].split(".")))
        days[1] += term[privacy[1]]
        if days[1] > 12:
            if days[1] % 12 == 0:
                days[0] += days[1] // 12 - 1
                days[1] = 12
            else:
                days[0] += days[1] // 12
                days[1] %= 12
        print(days)
        if days[0] < today[0]:
            result.append(i+1)
        if days[0] == today[0] and days[1] < today[1]:
            result.append(i+1)
        if days[0] == today[0] and days[1] == today[1] and days[2] <= today[2]:
            result.append(i+1)
    return result