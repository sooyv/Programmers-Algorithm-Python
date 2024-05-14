# 나의 풀이
# i가 isupper(), 즉 대문자이면, i.lower() 소문자로 바꾸어주고, 아니라면 i.upper() 대문자로 변환
def solution(my_string):
    answer = ''
    for i in my_string:
        answer += i.lower() if i.isupper() else i.upper()
    return answer



# 다른 사람의 풀이
# swapcase() 대소문자 상호 전환, 소문자는 대문자로, 대문자는 소문자로 전환해준다
def solution(my_string):
    return my_string.swapcase()