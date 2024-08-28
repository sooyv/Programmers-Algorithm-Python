# 첫번째 풀이
# sum(num_list[::2]) => num_list를 짝수 번째만 반환한 값을 sum
# sum(num_list[1::2]) => num_list의 홀수 번재만 반환한 값을 sum
# 삼항연산자를 통해서 큰 값을 return
def solution(num_list):
    return sum(num_list[::2]) if sum(num_list[::2]) > sum(num_list[1::2]) else sum(num_list[1::2])


# 다른 사람의 풀이
# max를 이용한 방법
def solution(num_list):
    return max(sum(num_list[::2]), sum(num_list[1::2]))