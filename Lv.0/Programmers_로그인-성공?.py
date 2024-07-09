# 나의 풀이
def solution(id_pw, db):
    # db를 순회하면서 각 요소 i의 0번째 인덱스를 확인
    for i in db:
        # 만약 id_pw[0]과 i[0] 즉, 아이디가 같다면,
        if i[0] == id_pw[0]:
            # 비밀번호가 같은지 확인하여 같다면 login return
            if i[1] == id_pw[1]:
                return "login"
            # 비밀번호가 같지 않다면 wrong pw return
            elif i[1] != id_pw[1]:
                return "wrong pw"
    # 일치하는 아이디가 없다면 fail return
    return "fail"   
    
    

# 다른 사람의 풀이 1
def solution(id_pw, db):
    # dict(db) - 딕셔너리로 변환하여 각 사용자 ID를 키로, 비밀번호를 값으로 한다.
    # dict(db)에서 get()으로 id_pw[0] 아이디 값을 찾고, 일치하는 키가 있다면, 값을 가져옴
    # :=(대입 표현식(Assignment Expression), 또는 Walrus Operator)를 통해 db_pw에 이름을 부여하고 재사용
    if db_pw := dict(db).get(id_pw[0]):
        # db_pw와 입력된 비밀번호 id_pw[1]을 비교하여 일치하면 "login" 반환
        # 일치하지 않으면 "wrong pw" 반환
        return "login" if db_pw == id_pw[1] else "wrong pw"
    # 아이디가 데이터베이스에 존재하지 않으면 "fail" 반환
    return "fail"