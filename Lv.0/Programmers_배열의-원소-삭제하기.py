# 나의 풀이
# filter 함수를 통해 arr 배열을 필터링한다.
# arr의 요소 x가 delete_list의 포함되지 않은 요소만 필터링
def solution(arr, delete_list):
    return list(filter(lambda x: x not in delete_list, arr))


# 다른 사람의 풀이
# delete_list을 순회하면서 delete_list의 i가 만약 arr 배열에 존재한다면,
# arr 배열에서 i를 제거한다(remove)
def solution(arr, delete_list):
    for i in delete_list:
        if i in arr:
            arr.remove(i)
    return arr