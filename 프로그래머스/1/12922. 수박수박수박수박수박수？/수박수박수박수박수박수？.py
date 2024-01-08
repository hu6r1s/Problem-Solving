def solution(n):
    subak = ""
    for i in range(n):
        if i % 2 == 0:
            subak += "수"
        else:
            subak += "박"
    return subak