# 나의 풀이
# lstrip을 사용해서 문자열의 맨 왼쪽에 0이 있다면 제거
def solution(n_str):
    return n_str.lstrip('0')



# 다른 사람의 풀이 1
# int(n_str)를 통해서 n_str을 정수로 변환한다. 이 과정에서 숫자 앞의 불필요한 0이 제거된다.
# 변환한 정수를 다시 str() 문자열로 변환하여 return 한다.
def solution(n_str):
    return str(int(n_str))


# 다른 사람의 풀이 2
# strip를 모른다고 할때 적절한 풀이라고 생각했다.
# n_str 문자열의 길이만큼 for문을 순회하면서 n_str[i]가 0이 아니라면 
# n_str[i:] 해당 인덱스부터 끝까지 잘라서 반환

# for문을 순회하는 도중 0이 아닌 인덱스가 나온다면 해당 인덱스부터 마지막 인덱스까지를 slicing해서
# return함으로 왼쪽에 존재하는 0만을 제거할 수 있다.
def solution(n_str):
    for i in range(len(n_str)):
        if n_str[i] != "0":
            return n_str[i:]
