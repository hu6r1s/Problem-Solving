import string

def solution(s, skip, index):
    alpa = sorted(set(string.ascii_lowercase) - set(skip))
    result = ""
    for i in s:
        result += alpa[(alpa.index(i) + index) % len(alpa)]
        
    return result