# 나의 풀이
# 삼항연산자로 풀이. num_list[-1]와 num_list[-2]로 num_list의 마지막 원소와 그 전 원소를 비교
# 마지막 원소가 그전 원소보다 크면 마지막 원소에서 그전 원소를 뺀 값을 num_list에 추가
# 마지막 원소가 그전 원소보다 크지 않다면 마지막 원소를 두 배한 값을 추가
# 값을 추가하여 새로운 리스트를 반환
def solution(num_list):
    return num_list + [num_list[-1] - num_list[-2]] if num_list[-1] > num_list[-2] else num_list + [num_list[-1] * 2]


# 다른 사람의 풀이
# append() 메서드를 사용하여 리스트에 새로운 값을 추가한 후에, 기존 리스트를 그대로 반환
def solution(l):
    l.append(l[-1] - l[-2] if l[-1] > l[-2] else l[-1] * 2)
    return l