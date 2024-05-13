import math

def solution(num_list):
    len_list = len(num_list)
    if len_list >= 11:
        return sum(num_list)
    else:
        return math.prod(num_list)