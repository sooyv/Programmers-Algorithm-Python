# 첫번째 풀이
def solution(a, b):
    # a와 b를 각각 문자열로 변환한 뒤 이어붙인다
    ab = str(a) + str(b)
    ba = str(b) + str(a)   
    # 두 수를 삼항연산으로 비교하여 큰 수를 반환
    return int(ab) if int(ab) > int(ba) else int(ba)


# 두번째 풀이 - max를 통해 최댓값 찾기
# # a와 b를 각각 문자열로 변환한 뒤 이어붙인 후, max를 통해 조금 더 간단히 최댓값을 반환하는 코드로 변경해 보았다.
def solution(a, b):
    return max(int(str(a) + str(b)), int(str(b) + str(a)))



# 다른 사람의 풀이
def solution(a, b):
    return int(max(f"{a}{b}", f"{b}{a}"))

# 이 풀이를 통해서 f-string에 대해서 알게 되었다.
# f-string은 문자열 내에 중괄호 {}를 사용하여 변수를 삽입할 수 있는 기능을 제공한다.
# 두 수를 이어붙여 만든 값 중 가장 큰 값을 간단하게 반환할 수 있다.
# f-string에 대해 더 자세히 알아보기 : https://peps.python.org/pep-0498/#how-to-denote-f-strings
