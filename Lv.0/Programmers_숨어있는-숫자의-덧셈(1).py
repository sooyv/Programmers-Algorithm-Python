# 나의 풀이 1
# isdigit() 함수 사용
# my_string을 하나씩 순회하며 isdigit()로 정수인지 확인
# 정수라면 answer에 더하여 return
def solution(my_string):
    answer = 0
    for i in my_string:
        if i.isdigit() == True :
            answer += int(i)
    return answer


# 더 간단히 풀이
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())




# 다른 사람의 풀이 1
# try-except 구문 사용
# try문에서 int(i)를 통해 정수로 변환할 수 있으면 answer에 더하고,
# 변환할 수 없을 경우 except 구문으로 넘어가 pass된다.
# 최종적으로 더해진 answer return
def solution(my_string):
    answer = 0
    for i in my_string:
        try:
            answer = answer + int(i)
        except:
            pass

    return answer


# 다른 사람의 풀이 2
# Regular Expression(정규 표현식)
# 문자열 my_string에서 1-9까지의 숫자가 아닌 것들을 제거하고 빈 문자('')로 대체
# sum()으로 반환된 숫자의 합을 계산
import re
def solution(my_string):
    return sum(int(n) for n in re.sub('[^1-9]', '', my_string))