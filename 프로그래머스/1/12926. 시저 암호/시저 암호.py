import string

def solution(s, n):
    result = ""
    low = string.ascii_lowercase
    up = string.ascii_uppercase
    for i in s:
        if i == " ":
            result += " "
        elif i in low:
            result += low[(low.index(i)+n)%len(low)]
        elif i in up:
            result += up[(up.index(i)+n)%len(up)]
    return result