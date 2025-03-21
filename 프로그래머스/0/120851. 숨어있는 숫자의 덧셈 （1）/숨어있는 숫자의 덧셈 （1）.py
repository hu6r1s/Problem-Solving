def solution(my_string):
    return sum([int(my) for my in my_string if my.isdigit()])