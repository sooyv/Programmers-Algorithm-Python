# 나의 풀이
# str_list의 각 요소에 대해 lambda x: ex not in x 조건을 적용하여,
# ex가 포함되지 않는 요소들만 필터링한다.
# 필터링한 리스트를 join으로 문자열로 반환한다.
def solution(str_list, ex):
    return ''.join(list(filter(lambda x : ex not in x, str_list)))



# 다른 사람의 풀이 1
# str_list의 각 문자열 s에 ex가 포함되지 않은 경우에만 filtered_list에 추가한다.
# filtered_list를 join하여 합친 문자열을 반환한다.
def solution(str_list, ex):
    filtered_list = [s for s in str_list if ex not in s]
    return "".join(filtered_list)


# 다른 사람의 풀이 2
# for문을 통해 str_list 배열을 순회하면서
# 만약 ex가 str_list의 요소 x에 포함되어 있다면, continue문을 통해 현재 반복을 건너뛴다.
# x가 ex를 포함하지 않는다면, x를 answer에 추가하여 합쳐진 문자열을 반환한다.
def solution(str_list, ex):
    answer = ''
    for x in str_list:
        if ex in x: continue
        answer+=x
    return answer