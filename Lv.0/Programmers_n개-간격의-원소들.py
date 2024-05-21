# 첫번째 풀이
# 0부터 num_list의 길이까지, n의 간격으로 떨어진 값을 answer에 append
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i])
    return answer


# 두번째 풀이
def solution(num_list, n):
    return [num_list[i] for i in range(0, len(num_list), n)]


# 세번째 풀이
# num_list를 처음부터 마지막 요소까지 n의 간격으로 return
def solution(num_list, n):
    return num_list[::n]