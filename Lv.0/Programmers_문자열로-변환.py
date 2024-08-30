# 첫번째 풀이: str() 사용
def solution(n):
    return str(n)


# 두번째 풀이:  f-string 사용
# 파이썬 3.6 이상에서 사용할 수 있는 문자열 포매팅
def solution(n):
    answer = f'{n}'
    return answer