# 첫번째 풀이
# for문 순회, 정수 n을 문자열로 변환
# answer에 정수 i를 더하여 return
def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer
    
    
# 두번째 풀이
def solution(n):
    return sum(int(i) for i in str(n))
    
    
    
# 다른 사람의 풀이 1
# divmod()로 n을 10으로 나누어 몫과 나머지를 각각 n과 r에 할당
# 나머지는 while문을 순회하며 answer에 더하고, n은 0이 아닐때까지 반복
# 나머지를 모두 더한 answer을 return
def solution(n):
    answer = 0
    while n:
        n, r = divmod(n, 10)
        answer += r
    return answer
