# 나의 풀이
# for문을 순회하면서 1부터 n+1까지 확인
# i를 2로 나눈 나머지가 1이라면 answer 배열에 i를 append
def solution(n):
    answer = []
    for i in range(1, n+1):
        if i % 2 == 1:
            answer.append(i)
    return answer

# 나의 풀이 2
def solution(n):
    return [i for i in range(1, n+1) if i % 2 == 1]

# 다른 사람의 풀이
# append 과정 없이 1부터 n+1까지 2씩 증가시킨 요소 i
# 즉, 홀수만 포함된 리스트를 생성
def solution(n):
    return [i for i in range(1, n+1, 2)]