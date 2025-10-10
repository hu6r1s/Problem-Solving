from collections import defaultdict

def solution(record):
    d = defaultdict(str)
    for rec in record:
        data = rec.split(" ")
        if data[0] == "Leave":
            continue
            
        d[data[1]] = data[2]
    
    result = []
    for rec in record:
        data = rec.split(" ")
        if data[0] == "Leave":
            result.append(f"{d[data[1]]}님이 나갔습니다.")
        elif data[0] == "Enter":
            result.append(f"{d[data[1]]}님이 들어왔습니다.")
    return result



"""
들어오고 나간 것이 기록 됨.
나갔다가 닉네임을 변경하면 기록의 닉네임도 변경됨
enter일 때, 딕셔너리(uid: nick)으로 넣음, 존재한다면 닉네임 변경
leave이면 pass, 
[(uid1234, Muzi), (uid4567, Prodo),]
["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
Enter uid1234 Muzi
Enter uid4567 Prodo
Leave uid1234
Prodo님이 들어왔습니다.
Ryan님이 들어왔습니다.
Prodo님이 나갔습니다.
Prodo님이 들어왔습니다.
"""