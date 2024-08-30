# 나의 풀이
# sort 메서드를 사용해서 원본 리스트를 정렬한 뒤, 6번째 요소 이후의 부분을 슬라이싱하여 반환
def solution(num_list):
    num_list.sort()
    return num_list[5:]


# 다른 사람의 풀이
# sorted 메서드를 사용해서 새로운 정렬된 리스트를 반환한뒤, 
# 정렬된 새로운 리스트에서 6번째 요소 이후의 부분을 슬라이싱하여 반환
def solution(num_list):
    return sorted(num_list)[5:]
