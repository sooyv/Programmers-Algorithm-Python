# 나의 풀이
# 삼항연산자를 통해 str1에 str2가 포함되어 있다면 1을, 아니라면 0을 반환
def solution(str1, str2):
    return 1 if str1 in str2 else 0


# 다른 사람의 풀이
# str1가 str2에 포함되어 있는지를 확인하여 True, False
# 논리값 True와 False를 정수로 변환하여 반환한다.
def solution(str1, str2):
    return int(str1 in str2)