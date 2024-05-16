# 나의 풀이
# array 배열의 max() 가장 큰 수, 그리고 그 수의 인덱스를 담은 배열을 return
def solution(array): 
    return [max(array), array.index(max(array))]