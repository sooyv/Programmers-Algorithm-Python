# 나의 풀이 1
# index_list에 있는 각 인덱스 i에 대해 my_string의 i번째 문자를 answer에 추가
def solution(my_string, index_list):
    answer = ''
    for i in index_list:
        answer += my_string[i]
    return answer


# 나의 풀이 2
# index_list의 각 인덱스 i에 대해 my_string의 i번째 문자를 추출하여
# 추출한 문자들을 join()으로 결합하여 return
def solution(my_string, index_list):
    return ''.join([my_string[i] for i in index_list])


# 다른 사람의 풀이
# map과 lambda로 index_list의 각 인덱스 x에 대해 my_string[x]에 해당하는 문자를 반환
# 추출한 문자들을 join()으로 하나의 문자열로 결합
def solution(my_string, index_list):
    return ''.join(map(lambda x: my_string[x], index_list))