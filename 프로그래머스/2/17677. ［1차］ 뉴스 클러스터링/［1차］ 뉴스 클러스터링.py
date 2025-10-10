from collections import Counter

def solution(str1, str2):
    str1, str2 = str1.lower(), str2.lower()
    cnt_str1, cnt_str2 = [], []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            cnt_str1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            cnt_str2.append(str2[i:i+2])
    print(Counter(cnt_str1) & Counter(cnt_str2))
    gyo = sum((Counter(cnt_str1) & Counter(cnt_str2)).values())
    hap = sum((Counter(cnt_str1) | Counter(cnt_str2)).values())
    jacard = 1 if not hap and not gyo else gyo / hap
    return int(jacard * 65536)