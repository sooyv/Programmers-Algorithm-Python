# 첫번째 풀이
# for문을 사용하여 array 배열의 i와 n이 같다면 answer을 증가
def solution(array, n):
    answer = 0
    for i in array:
        if i == n:
            answer += 1
    return answer



# 다른 사람의 풀이 1
# count 함수를 통해 배열 array에 존재하는 n값을 count해 return
def solution(array, n):
    return array.count(n)

# 다른 사람의 풀이 2
# [expression for item in iterable if condition] 리스트 컴프리헨션
# expression: 각 요소에 대한 계산식이나 표현식
# item: 이터러블(iterable)에서 가져온 각 요소
# iterable: 순회 가능한 객체입니다. (예: 리스트, 튜플, 집합, 문자열 등)
# condition (선택 사항): 각 요소를 포함할지 여부를 결정하는 조건

# 리스트 array의 각 요소 x에 대해서 조건 x == n을 만족하는 경우에는 1을 반환하고
# sum()으로 리스트 컴프리헨션으로 생성된 모든 값을 합산
def solution(array, n):
    return sum(1 for x in array if x == n)