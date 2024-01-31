def solution(s):
    s = s.lower()
    jaden = s.split(" ")
    result = ""
    for j in jaden:
        if j == "":
            result += ""
        else:
            result += j[0].upper() + j[1:].lower()
        result += " "
    return result[:-1]