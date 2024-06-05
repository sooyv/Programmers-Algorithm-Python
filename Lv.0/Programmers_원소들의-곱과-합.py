# 나의 풀이
# for문을 통해서 num_list의 모든 요소의 곱(multiply)을 구한다.
# 삼항연산자를 통해서 모든 요소들의 곱인 multiply과 모든 요소의 합의 제곱을 비교
# 모든 요소의 합의 제곱(sum(num_list)**2)이 multiply보다 크다면 1을 반환하고, 아니라면 0을 반환한다.
def solution(num_list):
    multiply = 1
    for i in num_list:
        multiply = multiply * i
        
    return 1 if sum(num_list)**2 > multiply else 0


# 다른 사람의 풀이 1
# s는 모든 요소의 합의 제곱
# m은 for문에서 리스트의 각 요소를 문자열로 변환하고, *를 사용해서 join한 문자열을 eval 함수로 계산
# 모든 요소를 더하여 제곱한 값 s가 모든 원소들의 곱 m보다 크다면 1을 반환하고, 아니라면 0을 반환
def solution(num_list):
    s = sum(num_list)**2
    m = eval('*'.join([str(n) for n in num_list]))
    return 1 if s > m else 0


# 다른 사람의 풀이 2
# 모든 요소의 곱하기 결과값을 나타낼 변수 multiply와, 모든 요소의 합의 제곱을 나타낼 plus 변수
# for문을 통해 num_list의 각 요소를 multiply에는 곱하고, plus에는 더함
# multiply이 plus의 제곱보다 작으면 1을 반환, 아니라면 0을 반환
def solution(num_list):
    multiply = 1
    plus = 0
    for x in num_list:
        multiply *= x
        plus += x
    if multiply < plus * plus: return 1
    return 0