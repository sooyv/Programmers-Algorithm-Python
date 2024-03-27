# 첫번째 풀이
# num1을 num2로 나눈 값을 a에 할당
# a에 1000을 곱하고 int()를 통해 정수부만 반환 
def solution(num1, num2):
    a = num1 / num2
    return int(a * 1000)


# 더 간단하게 풀이
def solution(num1, num2):
    return int(num1 / num2 * 1000)


# 다른 사람의 풀이 1
# num1을 num2로 나눈 값에 1,000을 곱한 값을 answer에 저장
# answer // 1을 통하여 정수부만 반환
def solution(num1, num2):
    answer = (num1 / num2) * 1000
    return answer // 1


# 다른 사람의 풀이 2
# 인수 x에 1000을 곱하여 x를 1000배로 만든 후, 
# // y를 통해 나누어 몫을 구해줌
solution = lambda x, y: 1000 * x // y