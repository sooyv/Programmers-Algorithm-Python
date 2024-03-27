# 나의 풀이 1
def solution(num1, num2):
    answer = -1
    if num1 == num2:
        answer = 1
    return answer
    
    
# 나의 풀이 2
# 삼항연산자 풀이
# <조건이 참일 때 값> if <조건식> else <조건이 거짓일 때 값>
def solution(num1, num2):
    return 1 if num1 == num2 else -1


# 다른 사람의 풀이 1
# python 특성상 두 수를 비교했을때 같으면 true 1, 다르면 false 0이 나오기 때문에,
# 참인지 거짓인지에 따라 나오는 값에 0.5를 빼고 * 2로, 두 수가 같으면 1 다르면 -1을 retrun
def solution(num1, num2):
    return ((num1 == num2) - 0.5) * 2




# 다른 사람의 풀이 2
# num1과 num2를 비교, 같다면 1, 다르다면 0이 리스트에 담김
# sum()으로 리스트의 요소를 모두 더하고, 같다면 1 * 2 -1으로 1이 return
# 다르다면 0 * 2 -1로 -1이 return
def solution(num1, num2):
    return sum([num1 == num2]) * 2 - 1