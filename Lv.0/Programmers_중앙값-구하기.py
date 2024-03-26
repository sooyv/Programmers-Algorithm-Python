# 나의 풀이
# sorted() 함수로 리스트를 정렬한 새로운 리스트를 반환
# 리스트의 길이를 2로 나눈 몫을 통해 가운데에 위치한 인덱스를 반환
def solution(array):
    return sorted(array)[len(array) // 2]