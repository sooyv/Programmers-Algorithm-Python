# 첫번째 풀이
# num_list의 길이가 11이상이면 num_list를 모두 더한값 return, sum(num_list)
# 아니라면, num_list의 요소를 모두 곱한 값 answer을 return
def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        answer = 1
        for i in num_list:
            answer *= i
        return answer
    

# 두 번째 풀이
# math 모듈의 prod() 함수를 사용
# 삼항연산자를 통해 num_list의 길이가 11이상이면, sum(num_list) 합을 return
# 아니라면 prod(num_list) 곱을 return
from math import prod
def solution(num_list):
    return sum(num_list) if len(num_list) >= 11 else prod(num_list)



# 다른 사람의 풀이
# num_list가 11보다 클 경우,
# num_list를 str 문자열로 만든 후, join()으로 리스트의 요소를 
# '+' 기호로 연결하여 하나의 문자열로 만든다.
# eval() 함수를 사용해 모두 더함
# 11 미만일 경우, eval() 함수를 사용해 모두 곱함
def solution(num_list):
    if len(num_list) >= 11:
        return eval('+'.join(list(map(str, num_list))))
    else:
        return eval('*'.join(list(map(str, num_list))))
