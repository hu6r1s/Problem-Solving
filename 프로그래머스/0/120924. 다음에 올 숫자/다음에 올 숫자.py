def solution(common):
    if common[-1] - common[-2] == common[1] - common[0]:
        return (common[-1] - common[-2]) + common[-1]
    elif common[-1] // common[-2] == common[1] // common[0]:
        return (common[-1] // common[-2]) * common[-1]