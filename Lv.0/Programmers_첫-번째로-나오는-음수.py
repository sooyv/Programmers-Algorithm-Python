# for문을 통해 num_list를 순회하며 
# if문으로 가장 처음 나오는 음수를 확인하여 인덱스를 return
# for문을 모두 순회한 뒤에도 리스트에 음수가 없다면 -1를 return
def solution(num_list):
    for i in range(0, len(num_list)):
        if num_list[i] < 0:
            return i
    return -1


# 다른 사람의 풀이 1
# 리스트 컴프리헨션 사용. num_list에서 가장 처음나오는 음수의 인덱스 i를 검사하여 리스트로 반환
# 만약 리스트 컴프리헨션이 빈 리스트를 반환하면, or 연산자의 오른쪽 값 [-1]를 return 한다.
# 선택된 리스트의 0번째 인덱스를 return
def solution(num_list):
    return ([i for i in range(len(num_list)) if num_list[i] < 0] or [-1])[0]


# 다른 사람의 풀이 2
# enumerate() 함수 : 기본적으로 인덱스와 원소로 이루어진 튜플(tuple)을 만들어 주는 함수.
# for i, num으로 인자를 풀어 인덱스와 원소를 각각 다른 변수에 할당
# if문을 통해 음수를 확인 후 첫번째 나오는 음수를 return
# num_list를 모두 순회 후에도 음수가 없다면 -1을 return
def solution(num_list):
    for i, num in enumerate(num_list):
        if num < 0:
            return i
    return -1