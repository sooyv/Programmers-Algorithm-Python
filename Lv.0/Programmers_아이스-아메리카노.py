# 나의 풀이
def solution(money):
    answer = [money // 5500, money % 5500]
    return answer


# 다른 사람의 풀이
# divmod(): 첫번째 숫자를 두번째 숫자로 나눈 몫과 나머지를 튜플(tuple) 형태로 반환
def solution(money):
    return divmod(money, 5500)