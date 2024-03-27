# 나의 풀이
def solution(num1, num2):
    return num1 % num2

# 더 간단히 풀이
solution = lambda num1, num2 : num1 % num2



# 다른 사람의 풀이 1
# divmod 함수는 몫과 나머지를 동시에 구할 수 있음
# 튜플의 첫 번째 요소는 몫이고, 두 번째 요소는 나머지이므로, [1]로 나머지를 구함
def solution(num1, num2):
    return divmod(num1, num2)[1]


# 다른 사람의 풀이 2
# while으로 num1이 num2보다 크거나 같은 동안에만 반복
# num1에서 num2의 값을 빼는 것을 반복하여 나머지를 구함
def solution(num1, num2):
    while num1 >= num2:
        num1 -= num2
    return num1