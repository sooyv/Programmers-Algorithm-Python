# 나의 풀이
# 리스트 컴프리헨션을 사용한 풀이
# start_num부터 end_num + 1까지의 숫자 i를 리스트로 변환하여 return
def solution(start_num, end_num):
    return [i for i in range(start_num, end_num + 1)]


# 다른 사람의 풀이
# range(start_num, end_num +1)까지의 숫자를 생성
# 생성한 숫자를 list()로 변환하여 return
def solution(start_num, end_num):
    return list(range(start_num, end_num + 1))