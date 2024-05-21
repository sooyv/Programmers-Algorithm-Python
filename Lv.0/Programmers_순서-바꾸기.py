# 나의 풀이
# num_list를 n번째 원소 이후의 원소들을 slice해서 n번째까지 slice한 원소들 앞에 +
def solution(num_list, n):
     return num_list[n:] + num_list[:n]