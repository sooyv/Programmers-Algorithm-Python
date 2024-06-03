# 나의 풀이
# "w", "a", "s", "d"를 Key로, 각 문자에 따라 바꾸는 값을 value로 딕셔너리 생성
# for문을 통해 control의 각 문자를 확인하며 dic에 존재하는 key값과 매치하여 n에 value값을 더해줌
def solution(n, control):
    dic = {"w" : 1, "s" : -1, "d" : 10, "a" : -10}
    for i in control:
        n += dic[i]
    
    return n



# 다른 사람의 풀이 1
# zip() 함수를 사용하여 각 제어 문자와 해당 값을 묶어서 딕셔너리 key를 생성
# 리스트 컴프리헨션을 사용하여 control의 각 문자 c에 대해 딕셔너리 key에서 해당 문자의 value를 가져옴
# 가져온 value를 sum()으로 더하고, n에 합산해 return
def solution(n, control):
    key = dict(zip(['w','s','d','a'], [1,-1,10,-10]))
    return n + sum([key[c] for c in control])


# 다른 사람의 풀이 2
# count()는 찾고 싶은 문자의 갯수를 찾을 수 있다.
# 'd'는 +10이고, 'a'는 -10, 'w'는 +1이고 's'는 -1이다.
# 'd'의 갯수에서 'a'의 갯수를 뺀 결과에 10을 곱해서 n에 더한다.
# 'w'의 갯수에서 's'의 갯수를 뺀 결과를 n에 더한다.
def solution(n, control):
    return n + 10 * (control.count('d') - control.count('a')) + (control.count('w') - control.count('s'))