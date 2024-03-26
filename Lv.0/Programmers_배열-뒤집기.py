# 나의 풀이
# 리스트.reverse(), 리스트 함수
# 주의 사항 : 반환값이 None, 해당 리스트의 원형 변경.
def solution(num_list):
    num_list.reverse()
    return num_list


# 두번째 풀이
# reversed는 파이썬 내장 함수, 리스트, 튜플, 딕셔너리 사용가능
# 해당 객체의 원형을 바꾸지 않는다.
def solution(num_list):
    return list(reversed(num_list))


# 다른 사람의 풀이
# 슬라이싱을 사용 : list[start:stop:step]
# start : 시작인덱스, stop: 종료인덱스, step: 슬라이스 간격
# start와 stop을 생략하고 step을 -1로 설정하여 리스트를 역순으로 변경.
def solution(num_list):
    return num_list[::-1]