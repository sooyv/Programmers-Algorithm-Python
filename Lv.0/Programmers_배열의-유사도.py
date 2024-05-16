# 나의 풀이 1
# for문을 순회한다. 첫번째 for문은 s1에 char1를 확인하고
# 두번째 for문은 s2에서 char2를 확인한다.
# if문으로 char1과 char2가 같은지 확인하고, 같다면 answer를 1 증가시킨다.
def solution(s1, s2):
    answer = 0
    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                answer += 1
    return answer

# 나의 풀이 2
# for 루프를 통해 첫 번째 문자열 s1의 각 문자를 순회하면서 
# if문으로 s2에 char1가 존재하는지 확인하고,
# 존재한다면 answer를 1 증가시킨다.
def solution(s1, s2):
    answer = 0
    for char1 in s1:
        if char1 in s2:
            answer += 1
        else:
            continue
    return answer



# 다른 사람의 풀이
# set()을 이용해서 중복을 제거, & 연산자를 사용하여 두 집합의 교집합을 구한 후
# len()으로 교집합의 갯수를 구함.
def solution(s1, s2):
    return len(set(s1) & set(s2));