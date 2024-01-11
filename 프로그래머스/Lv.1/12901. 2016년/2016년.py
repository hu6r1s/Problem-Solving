def solution(a, b):
    cal = {1: "FRI", 2: "SAT", 3: "SUN", 4: "MON", 5: "TUE", 6: "WED", 0: "THU"}
    s = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = 0
    for i in range(a-1):
        count += s[i]
    count += b
    return cal[count % 7]