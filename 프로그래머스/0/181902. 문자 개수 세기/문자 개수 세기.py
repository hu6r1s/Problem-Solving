import string
from collections import defaultdict

def solution(my_string):
    dic = defaultdict(int)
    for letter in string.ascii_letters:
        dic[letter] = 0
    for s in my_string:
        dic[s] += 1
    return [value for _, value in sorted(dic.items())]