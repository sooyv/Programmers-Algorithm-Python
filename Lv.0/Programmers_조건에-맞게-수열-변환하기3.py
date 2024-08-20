# 나의 풀이
# 삼항 연산자를 통해서 k % 2 != 0, 즉, k가 홀수라면 x * k한 list를 반환
# k가 짝수라면 x + k한 list를 반환
def solution(arr, k):
    return list(map(lambda x: x * k, arr)) if k % 2 != 0 else list(map(lambda x: x + k, arr))


# 다른 사람의 풀이
# for i in arr로 arr 배열의 각 요소를 순차적으로 가져와 i에 할당
#  k % 2 != 0, 즉 k가 홀수라면 i * k가 계산되고, 짝수라면 i + k가 계산되어 반환
def solution(arr, k):
    return [i * k if k % 2 != 0 else i + k for i in arr]