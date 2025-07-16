def solution(babbling):
    cnt = 0
    ong = ["aya", "ye", "woo", "ma"]
    for bab in babbling:
        for i in ong:
            bab = bab.replace(i, "*")
        if set(bab) == {"*"}:
            cnt += 1
    return cnt