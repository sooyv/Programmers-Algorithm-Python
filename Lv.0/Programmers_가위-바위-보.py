# 첫번째 풀이
def solution(rsp):
    answer = ''
    for i in rsp:
        if i == '2':
            answer += '0'
        elif i == '0':
            answer += '5'
        elif i == '5':
            answer += '2'
    return answer


# 다른 사람의 풀이 1
# 사전 d를 통해서 문자열 rsp가 2일때 0으로, 0일때 5로, 5일때 2로 변환
# for문을 순회하면서 d[i]값이 키일때 값을 반환하여 join('')
def solution(rsp):
    d = {'0':'5','2':'0','5':'2'}
    return ''.join(d[i] for i in rsp)


# 다른 사람의 풀이 2
# rsp에서 숫자 2/5/0을 각각 s/p/r로 대체하고, 
# 그 후에 r -> 5 / s-> 0 / p -> 2로 다시 대체
def solution(rsp):
    rsp = rsp.replace('2','s')
    rsp = rsp.replace('5','p')
    rsp = rsp.replace('0','r')
    rsp = rsp.replace('r','5')
    rsp = rsp.replace('s','0')
    rsp = rsp.replace('p','2')
    return rsp