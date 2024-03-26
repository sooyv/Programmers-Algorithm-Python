# 나의 풀이
def solution(num1, num2):
    return num1 // num2


# 다른 사람의 풀이 1
# 이 풀이를 통해서 연산 특수 메서드에 대해서 알게 되었다.
# a // b  ->  __floordiv__(self, other)
solution = int.__floordiv__


# 다른 사람의 풀이 2
# 실수 형태의 나눗셈 결과 answer를 int(answer)를 통해 정수형(int)으로 변환하여 반환
def solution(num1, num2):
    answer = num1 / num2
    return int(answer)
