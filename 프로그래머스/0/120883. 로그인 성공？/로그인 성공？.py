def solution(id_pw, db):
    for data in db:
        if id_pw[0] == data[0] and id_pw[1] == data[1]:
            return "login"
    else:
        if all(id_pw[0] != data[0] for data in db):
            return 'fail'
        if all(id_pw[1] != data[1] for data in db if id_pw[0] == data[0]):
            return 'wrong pw'