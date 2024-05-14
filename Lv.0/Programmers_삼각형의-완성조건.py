# 나의 풀이
# sort(reverse=True)로 내림차순으로 정렬
# 가장 큰 수인 sides[0]이 나머지 두 원소 sides[1] + sides[2]를 더한 값보다 크거나 같으면
# 2를 return, 아니라면 1을 return
def solution(sides):
    sides.sort(reverse=True)
    return 2 if sides[0] >= sides[1] + sides[2] else 1



# 다른 사람의 풀이
# 삼각형이 되기 위한 조건: 세 변의 총합 - 최대 변 길이 > 최대 변 길이
# 삼각형이 되기 위한 조건에 의해서 세 변의 총 합에서 최대 변 길이를 뺀 값이 최대 변 길이보다 크다면
# 삼각형을 만들 수 있으므로 1을 return 아니라면, 2를 return
def solution(sides):
    return 1 if max(sides) < (sum(sides) - max(sides)) else 2