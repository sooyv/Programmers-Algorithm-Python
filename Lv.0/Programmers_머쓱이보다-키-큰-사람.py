# 나의 풀이
# 이전의 다른 사람의 풀이에서 본 리스트 컴프리헨션 활용하기
# array 배열의 요소 i가 height 보다 크다면 1,
# sum() 함수로 모든 1을 더하여 return
def solution(array, height):
    return sum(1 for i in array if i > height)


# 다른 사람의 풀이
# array 배열에 height를 추가,
# sort(reverse=True)를 통해서 내림차순으로 정렬
# 내림차순으로 정렬된 array에서 height의 index를 확인하여 머쓱이가 몇번째인지 확인함
# 즉, 머쓱이보다 키가 큰 사람 수를 return
def solution(array, height):
    array.append(height)
    array.sort(reverse=True)
    return array.index(height)