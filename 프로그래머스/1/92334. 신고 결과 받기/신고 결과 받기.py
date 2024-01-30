def solution(id_list, report, k):
    singo = dict()
    id = dict()
    for i in id_list:
        singo[i] = 0
        id[i] = []
    report = set(report)
    for r in report:
        id[r.split()[0]].append(r.split()[1])
        singo[r.split()[1]] += 1
    jungji = []
    for s in singo.keys():
        if singo[s] >= k:
            jungji.append(s)
    result = []
    for i in id:
        count = 0
        for j in jungji:
            if j in id[i]:
                count += 1
        result.append(count)
    return result
    