# 나의 풀이
# for문으로 strlist의 각각의 요소에 접근,
# len 함수로 길이 변환하여 result 배열에 append
def solution(strlist):
    result = []
    for i in strlist:
        result.append(len(i))
    return result


# 두번째 풀이
# map을 이용하여 요소에 적용할 len 함수를 통해 map 객체 생성,
# 생성한 map 객체를 list()로 형변환
def solution(strlist):
    answer = list(map(len, strlist))
    return answer

# +++ python의 map 함수 +++
# map(function, iterable)
# function: 각 요소에 적용할 함수
# irerable: 반복 가능한 요소

# map 함수의 반환 값은 map객체이기 때문에 해당 자료형을 list나 tuple로 형 변환 필요