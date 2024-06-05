# 나의 풀이
# for문을 통해서 요소 i가 홀수라면 odd에 이어붙이고, 짝수라면 even에 이어붙인다.
# 두 수의 합을 return
def solution(num_list):
    odd = ''
    even = ''
    for i in num_list:
        if i % 2 == 0:
            print(i)
            even += str(i)
        else:
            odd += str(i)
    return int(odd) + int(even)