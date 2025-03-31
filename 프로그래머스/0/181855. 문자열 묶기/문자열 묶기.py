from collections import defaultdict

def solution(strArr):
    dic = defaultdict(int)
    for a in strArr:
        dic[len(a)] += 1
    return max(dic.values())