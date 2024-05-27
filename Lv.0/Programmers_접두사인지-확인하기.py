# 나의 풀이
# 삼항연산자로 my_string.find(is_prefix)를 통해 my_string에서 is_prefix를 찾은
# 인덱스가 0번째 즉, 접두사가 맞으면 1을 return하고, 아니라면 0을 return
def solution(my_string, is_prefix):
    return 1 if my_string.find(is_prefix) == 0 else 0



# 다른 사람의 풀이
# startswith: 현재 문자열(my_string)이 사용자가 지정하는 특정 문자(is_prefix)로 시작하는지 확인하는 함수
# my_string이 is_prefix로 시작한다면 True로 int정수값 1이 return
# is_prefix로 시작하지 않는다면 False로 int정수값 0이 return
def solution(my_string, is_prefix):
    return int(my_string.startswith(is_prefix))