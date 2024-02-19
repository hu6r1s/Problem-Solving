import math

def solution(fees, records):
    rec = dict()
    result = []
    for record in records:
        re = record.split()
        h, m = re[0].split(":")
        if re[2] == "IN":
            if re[1] not in rec.keys():
                rec[re[1]] = [int(h)*60+int(m), 0]
            else:
                rec[re[1]][0] += int(h) * 60 + int(m)
        elif re[2] == "OUT":
            rec[re[1]][1] += int(h) * 60 + int(m)
    for r in rec.keys():
        if rec[r][1] <= rec[r][0]:
            rec[r][1] += 1439
    rec = dict(sorted(rec.items()))
    for r in rec.keys():
        time = rec[r][1] - rec[r][0]
        if time > fees[0]:
            total = fees[1] + math.ceil((time-fees[0])/fees[2]) * fees[3]
        else:
            total = fees[1]
        result.append(total)
    return result