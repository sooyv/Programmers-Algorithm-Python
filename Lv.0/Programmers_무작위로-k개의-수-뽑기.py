# 나의 풀이 1
# 배열 arr을 순회하면서 result에 arr의 요소 value가 없다면 append
def solution(arr, k):
    result = []
    for value in arr:
        if value not in result:
            result.append(value)
    
    # result 배열의 길이가 k보다 작다면, 작은만큼 -1을 append
    while len(result) < k:
        result.append(-1)
        
    # k까지의 길이의 result 배열을 return
    return result[:k]


# 나의 풀이 2
def solution(arr, k):
    result = []
    for v in arr:
        if v not in result:
            result.append(v)
            
    # result 배열의 길이가 k보다 작다면, 작은만큼
    # extend()를 통해 배열의 끝에 -1이 추가
    if len(result) < k:
        result.extend([-1] * (k - len(result)))
        
    return result[:k]




# 다른 사람의 풀이
def solution(arr, k):
    ret = []
    for i in arr:
        if i not in ret:
            ret.append(i)
        # 배열 ret의 길이가 k와 같다면 break
        if len(ret) == k:
            break

    # ret의 길이가 k보다 작으면, (k - len(ret))만큼 -1을 채움
    return ret + [-1] * (k - len(ret))