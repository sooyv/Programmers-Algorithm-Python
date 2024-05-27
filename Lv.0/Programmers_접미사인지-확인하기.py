# 나의 풀이 1
# endswith 함수를 통해 정의된 문자열이 지정된 접미사로 끝나면 True를 돌려주고, 그렇지 않으면 False
# return 된 값을 int()로 변환하여 반환
def solution(my_string, is_suffix):
    return int(my_string.endswith(is_suffix))


# 나의 풀이 2
# [::-1]로 뒤집은 문자열 my_string에서 뒤집은 is_suffix가 존재하는 인덱스가 0이라면,
# 본래의 뒤집지 않은 문자열에서는 접미사가 맞기 때문에 1을 return. 인덱스가 0이 아니라면 0을 return
def solution(my_string, is_suffix):
    return 1 if (my_string[::-1]).find(is_suffix[::-1]) == 0 else 0



# 다른 사람의 풀이
# my_string 문자열의 끝에서 len(is_suffix) 길이 만큼의 부분 문자열을 추출
# 추출된 문자열이 is_suffix와 같은지 비교하여 맞다면 1을 return, 아니라면 0을 return
def solution(my_string, is_suffix):
    print(my_string[-3:])
    if my_string[-len(is_suffix):] == is_suffix : return 1
    return 0