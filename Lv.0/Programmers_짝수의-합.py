# 첫 번째 풀이
# i를 2로 나눈 나머지가 0인지 확인하여, 짝수만 answer에 더함
def solution(n):
    answer = 0
    for i in range(0, n+1):
        if (i % 2 == 0):
            answer += i
    return answer


# 두 번째 풀이
# 0부터 n까지 2씩 증가하는 모든 값, 짝수만 더함
def solution(n):
    answer = 0
    for i in range(0, n+1, 2):
        answer += i
    return answer



# 다른 사람의 풀이
# range(start: stop: step)
# 0부터 n까지의 범위에서 2씩 증가하는 모든 짝수를 sum()을 통해 더하여 return
def solution(n):
    return sum(range(0, n+1, 2))