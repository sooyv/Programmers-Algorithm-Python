# 첫번째 풀이 - in 사용
# in을 통해서 my_string에 target이 있는지 확인하고 있다면 true, 없다면 false를 반환
# 반환한 값을 int로 변환해 1이나, 0을 최종적으로 반환한다.
def solution(my_string, target):
    return int(target in my_string)


# 두번째 풀이 - find() 함수 이용
# find(target) target의 인덱스를 반환. target이 있다면 인덱스의 수가 0보다 크므로
# 삼항 연산자를 통해 1을 return 하고 아니라면 0을 return 한다.
def solution(my_string, target):
    return 1 if my_string.find(target) >= 0 else 0