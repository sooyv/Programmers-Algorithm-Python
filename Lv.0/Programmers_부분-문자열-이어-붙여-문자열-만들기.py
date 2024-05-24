# 나의 풀이
# for문으로 my_strigns의 길이만큼 반복
# parts의 각 i번째 인덱스에서 start와 end를 확인
# my_strings의 i번째 문자열에서 start부터 end까지의 부분 문자열을 추출하여 answer에 +
def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        start, end = parts[i]
        answer += my_strings[i][start:end+1]
    return answer


# 다른 사람의 풀이 1
# enumerate(parts)를 사용하여 parts 리스트를 인덱스 i와 부분 인덱스 (s, e)로 반복
# my_strings의 i번째 문자열에서 s부터 e까지의 부분 문자열을 추출한다. (e+1로 마지막 문자열까지 추출)
# 모두 구한 answer를 return
def solution(my_strings, parts):
    answer = ''
    for i, (s, e) in enumerate(parts):
        answer += my_strings[i][s:e+1]
    return answer


# 다른 사람의 풀이 2
# zip(my_strings, parts)는 my_strings와 parts 리스트를 순회하며 x,y를 얻는다
# x는 my_strings의 각 요소이고, y는 parts의 각 요소인 슬라이싱 범위이다.
# y[0]는 시작 인덱스, y[1]는 끝 인덱스로 x[y[0]:y[1]+1]를 통해 문자열 x의 부분 문자열을 추출
def solution(my_strings, parts):
    return ''.join([x[y[0]:y[1]+1] for x,y in zip(my_strings, parts)])
