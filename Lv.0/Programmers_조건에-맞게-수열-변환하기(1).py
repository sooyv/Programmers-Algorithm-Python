# 나의 풀이
# if문 : 값이 50보다 크거나 같은 짝수라면 2로 나누고
# elif문 : 50보다 작은 홀수라면 2를 곱한다
# else문 : 둘다 아니라면 그냥 i를 append
def solution(arr):
    answer = []
    for i in arr:
        if i >= 50 and i % 2 == 0:
            answer.append(i // 2)
        elif i < 50 and not i % 2 == 0:
            answer.append(i * 2)
        else:
            answer.append(i)
    return answer