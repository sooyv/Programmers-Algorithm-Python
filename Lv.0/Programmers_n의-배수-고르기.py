# 나의 풀이
# for문 순회하며 numlist에서 각 요소 확인
# if문에서 요소를 n으로 나누었을때 나머지가 0이라면, answer에 추가
def solution(n, numlist):
    answer = []
    for i in numlist:
        if i % n == 0:
            answer.append(i)
    return answer


# 더 간단히 풀이
# 리스트 컴프리헨션을 이용해 풀이
def solution(n, numlist):
    return [i for i in numlist if i % n == 0]
    
    
    
# 다른 사람의 풀이
# lambda를 통해 numlist의 각 요소 v를 입력으로 받아 v가 n으로 나누어 떨어지는지 검사
# filter함수를 통해 True를 반환하는지 확인. 즉, v가 n으로 나누어 떨어지는지 확인
# list()로 함수의 반환 값을 리스트로 변환하여 반환
def solution(n, numlist):
    return list(filter(lambda v: v % n == 0, numlist))