# 나의 풀이
# k부터 n까지 k의 배수(k의 간격으로) 배열을 return
def solution(n, k):
    return [i for i in range(k, n+1, k)]