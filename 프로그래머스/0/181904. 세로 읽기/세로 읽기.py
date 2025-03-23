def solution(my_string, m, c):
    string = []
    for i in range(0, len(my_string), m):
        string.append(list(my_string[i:i+m]))
    return "".join(list(zip(*string))[c-1])