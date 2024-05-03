# 첫번째 풀이
# lambda를 통해서 numbers의 각 요소 x를 * 2배
# map함수로 list의 모든 요소에 함수를 적용한 결과 answer를 반환
def solution(numbers):
    answer = list(map(lambda x: x * 2, numbers))
    return answer


# 두번째 풀이
# for문을 사용하여 numbers의 각 요소 i를 *2
# answer 배열에 append하여 return
def solution(numbers):
    answer = []
    for i in numbers:
        answer.append(i * 2)
    return answer


# 다른 사람의 풀이
# [표현식 for 항목 in 반복가능객체 if 조건문] 형태를 "리스트 컴프리헨션"이라고 한다.
# 리스트(numbers)의 각 요소(num)에 대해 num * 2를 계산하여 새로운 리스트를 생성
def solution(numbers):
    return [num * 2 for num in numbers]
