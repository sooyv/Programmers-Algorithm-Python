# 첫 번째 풀이
# 리스트에 포함된 모든 숫자들의 합을 숫자들의 개수로 나누어 평균을 구함
def solution(numbers):
    return sum(numbers) / len(numbers)


# 두 번째 풀이
# numbers의 모든 합을 구하고, len으로 숫자들의 개수로 나누어 평균을 구함
def solution(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum / len(numbers)