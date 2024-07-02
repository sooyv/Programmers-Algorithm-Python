# message의 길이를 구한 후 * 2로 두 배로 만들기
def solution(message):
    return len(message) * 2



# 다른 사람의 풀이
# 비트 시프트 연산을 통한 풀이
# message의 길이를 구한 후 시프트 연산으로 두 배로 만들기
def solution(message):
    return len(message) << 1