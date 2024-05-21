# 첫번째 풀이
# num_list의 첫번째부터 n까지를 return
def solution(num_list, n):
    return num_list[:n]


# 두번째 풀이
# for문 순회로 answer배열에 n까지의 num_list요소를 append
def solution(num_list, n):
    answer = []
    for i in range(n):
        answer.append(num_list[i])
    return answer