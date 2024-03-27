# 나의 풀이 1
def solution(num1, num2):
    return num1 + num2

# 더 간단히 풀이
solution = lambda num1, num2 : num1 + num2

# 나의 풀이 2
# sum() 함수를 호출할 때는 인자로 리스트나 튜플을 전달해야함
def solution(num1, num2):
    return sum([num1, num2])


# 다른 사람의 풀이 1
# 람다 함수를 사용하여 가변 인자를 받고, sum을 이용해서 받은 모든 인자들의 합을 구함
solution = lambda * x : sum(x)