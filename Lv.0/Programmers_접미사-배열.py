# 나의 풀이
# my_string을 역순으로 순회하면서
# 현재 문자인 i를 suffix의 앞에 추가하고 answer 배열에 추가한다.
# 이렇게 모든 접미사가 모인 answer 배열을 sorted하여 정렬하고 return한다.
def solution(my_string):
    answer = []
    suffix = ''
    for i in reversed(my_string):
        suffix = i + suffix
        answer.append(suffix)
    return sorted(answer)


# 다른 사람의 풀이
# for in range문으로 my_string 문자열의 길이만큼을 반복하며 접미사를 구하는 코드

# range(len(my_string)) -  0부터 문자열의 길이까지를 생성한다.
# my_string[i:] -  문자열 my_string의 i번째 문자부터 끝까지의 부분 문자열을 반환
# sorted를 통해 전체 배열을 사전순으로 정렬 후 return
def solution(my_string):
    return sorted(my_string[i:] for i in range(len(my_string)))