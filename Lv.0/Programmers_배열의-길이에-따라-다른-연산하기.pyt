# 나의 풀이
# enumerate(arr)를 사용하여 배열 arr의 요소(x)와 인덱스(i)를 함께 가져옴
def solution(arr, n):
    # 짝수 길이의 배열 -> 홀수 번째 인덱스에 n을 더함
    if len(arr) % 2 == 0:
        return [x + n if i % 2 != 0 else x for i, x in enumerate(arr)]
    # 홀수 길이의 배열 -> 짝수 번째 인덱스에 n을 더함
    else:
        return [x + n if i % 2 == 0 else x for i, x in enumerate(arr)]

    
    
# 다른 사람의 풀이 1
def solution(arr, n):
    # arr 배열의 길이
    N = len(arr)
    # arr 배열의 길이를 2로 나눈 나머지가 1이면 (즉, 홀수이면)
    if N % 2:
        # 짝수 인덱스 - 0부터 시작해서 N보다 작은 수까지 2씩 증가하며 n을 더함
        for i in range(0, N, 2): 
            arr[i] += n
    else:
        # 홀수 인덱스 - 1부터 시작해서  N보다 작은 수까지 2씩 증가하며 n을 더함
        for i in range(1, N, 2): 
            arr[i] += n
    return arr


# 다른 사람의 풀이 2
# 삼항연산자를 이용한 풀이 
# if len(arr) % 2 != 0 (배열의 길이가 홀수인 경우, if 조건이 True인 경우)
# i % 2 == 0 (arr 배열의 짝수번째 인덱스)에 arr[i] + n, 짝수번째 인덱스가 아닌 arr 배열의 요소는 그대로 arr[i]를 반환

# if len(arr) % 2 != 0 (해당 조건이 False인 경우, 배열의 길이가 짝수인 경우)
# i % 2 != 0 (arr 배열의 홀수번째 인덱스)에 arr[i] + n, 홀수번째 인덱스가 아닌 arr 배열의 요소는 그대로 arr[i]
def solution(arr, n):
    return [arr[i] + n if i % 2 == 0 else arr[i] for i in range(len(arr))] if len(arr) % 2 != 0 else [arr[i] + n if i % 2 != 0 else arr[i] for i in range(len(arr))]
