# 나의 풀이
# while문을 통해 answer가 n보다 크거나 같을때까지 반복
# answer에 numbers의 각 요소를 차례대로 더함. 
# 반복마다 i + 1을 통해 numbers의 다음 요소를 더할 수 있도록 한다.
def solution(numbers, n):
    answer = 0
    i = 0
    while answer <= n:
        answer += numbers[i]
        i += 1
    return answer


# 다른 사람의 풀이
# for i in range(len(numbers))를 사용하여 배열의 각 인덱스에 대해 반복한다
# sum(numbers[:i + 1]) > n로 지금까지의 합계를 구하고 n보다 큰지 확인한다
# 만약 초과한다면, next() 함수를 사용하여 첫 번째 초과하는 합계를 반환
def solution(numbers, n):
    return next(sum(numbers[:i + 1]) for i in range(len(numbers)) if sum(numbers[:i + 1]) > n)
