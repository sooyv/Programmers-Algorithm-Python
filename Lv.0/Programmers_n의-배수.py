# 나의 풀이 1
# num에서 n을 나눈 나머지가 0이면 1을 return, 아니라면 0을 return
def solution(num, n):
    return 1 if num % n == 0 else 0

# 나의 풀이 2
# num에서 n을 나눈 나머지를 통해 true, false를 구분
# 이것을 int로 변환 시 1과 0으로 변환하여 return
def solution(num, n):
    return int(num % n == 0)


# 다른 사람의 풀이
# 논리 부정 연산 not()
# num에서 n을 나눈 나머지를 확인. 나머지가 0이라면 not(0)은 True
# 나머지가 1이라면 not(1)은 false
# 즉, 나머지가 0이라면 1을 return, 나머지가 1이라면 0을 return
def solution(num, n):
    return int(not(num % n))