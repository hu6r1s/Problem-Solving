from datetime import datetime

def solution(date1, date2):
    return 1 if (datetime(date2[0], date2[1], date2[2]) - datetime(date1[0], date1[1], date1[2])).days > 0 else 0