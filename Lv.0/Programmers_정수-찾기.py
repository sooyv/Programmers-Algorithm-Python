# 첫번째 풀이 - in 사용
# in 연산자를 사용하여 리스트 num_list에 값 n이 포함되어 있는지를 확인
# 있다면 true, 없다면 false가 반환되고, int로 true를 1로, false를 0으로 변환하여 반환
def solution(num_list, n):
    return int(n in num_list)

# 두번째 풀이 - __contains__ 사용
# 리스트 객체의 __contains__ 메서드를 사용하여 n이 포함되어 있는지를 확인
# 있다면 true, 없다면 false가 반환되고, int로 true를 1로, false를 0으로 변환하여 반환
def solution(num_list, n):
    return int(num_list.__contains__(n))