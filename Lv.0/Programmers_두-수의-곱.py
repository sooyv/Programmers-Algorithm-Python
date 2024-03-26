# 첫번째 풀이
def solution (num1, num2):
    return num1 * num2

# 두 번째 풀이
solution = lambda num1, num2 : num1 * num2

# 다른 사람의 풀이
# i가 num2보다 작은 동안 answer에 num1을 더함
# 즉, num2 횟수만큼 answer에 num1을 더하여 곱하기를 구현
# 예를 들어, num1이 3이고 num2가 4일 경우에는 3을 4번 더하는 것으로서 결과적으로 3 * 4 = 12
def solution(num1, num2):
    #return num1 * num2
    i = 0
    answer = 0
    while i < num2:
        answer += num1
        i += 1
    return answer
