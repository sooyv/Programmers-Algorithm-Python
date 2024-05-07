# 나의 풀이
# n을 7으로 나눈 값이 0이면 그 몫을 return
# 0이 아니라면 해당 몫보다 한판의 피자가 더 필요한 것이기 때문에 n // 7+1을 return
def solution(n):
    answer = 0
    if n % 7 == 0:
        return n // 7
    else:
        return n // 7 + 1

    
    
# 다른 사람의 풀이 1
#  n이 7로 나누어 떨어지지 않는 경우에도 n을 7로 나눈 몫에 1을 더한 값을 반환
#  n을 7로 나눈 몫을 구하고, 나머지가 있으면 몫에 1을 더하여 결과를 계산
def solution(n):
    return (n - 1) // 7 + 1


# 다른 사람의 풀이 2
# ceil : ceil 함수는 주어진 숫자를 올림하여 반환
# n을 7로 나눈 값에서 소수점 이하를 올림하여 정수로 return
import math

def solution(n):
    return math.ceil(n/7)