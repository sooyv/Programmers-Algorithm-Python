# 나의 풀이
# str(a) + str(b) 두 정수 a, b를 붙여서 쓴 값이 2 * a * b 보다 크거나 같을 경우
# int(str(a) + str(b))를 return. 아니라면 2 * a * b를 return
def solution(a, b):
    return int(str(a) + str(b)) if int(str(a) + str(b)) >= 2 * a * b else 2 * a * b

    
# 다른 사람의 풀이
# 두 정수 a, b를 붙여서 쓴 값과 2 * a * b 값 중, max값을 return
def solution(a, b):
    return max(int(str(a) + str(b)), 2 * a * b)