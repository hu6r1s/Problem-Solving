def solution(num_list):
    a, b = 0, 0
    for i in range(len(num_list)):
        if i % 2:
            a += num_list[i]
        else:
            b += num_list[i]
    if a > b:
        return a
    elif a == b:
        return a
    else:
        return b