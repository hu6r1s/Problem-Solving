from collections import defaultdict

def solution(a, b, c, d):
    dic = defaultdict(int)
    for i in [a, b, c, d]:
        dic[i] += 1
    
    dic = sorted(dic.items(), key=lambda x: (x[1], x[0]))

    if len(dic) == 1:
        return 1111 * dic[0][0]
    elif len(dic) == 2 and 3  == dic[1][1]:
        return (10 * dic[1][0] + dic[0][0]) ** 2
    elif len(dic) == 2 and 2 == dic[1][1]:
        return (dic[0][0] + dic[1][0]) * abs(dic[0][0] - dic[1][0])
    elif len(dic) == 3:
        a = [k for k, v in dic if v != 2]
        return a[0] * a[1]
    elif len(dic) == 4:
        return dic[0][0]
        