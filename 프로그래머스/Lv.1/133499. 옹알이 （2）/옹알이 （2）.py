def solution(babbling):
    b = ["aya", "ye", "woo", "ma"]
    count = 0
    for i in range(len(babbling)):
        for j in b:
            if j in babbling[i] and j * 2 not in babbling[i]:
                babbling[i] = babbling[i].replace(j, "*")
        if all(j == "*" for j in babbling[i]):
            count += 1
    return count