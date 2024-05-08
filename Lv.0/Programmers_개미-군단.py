# 첫번째 풀이
def solution(hp):
#   장군개미 5, 병정개미 3, 일개미 1
    ants = [5, 3, 1]
    answer = 0
    for i in ants:
        answer += hp // i
        hp = hp % i
        
    return answer


# 두번째 풀이
# divmod() 첫번째 숫자를 두번째 숫자로 나눈 몫과 나머지를 d와 hp에 각각 할당
# 총 몇마리의 개미가 필요한지 구하기 위해서 answer에 d를 더하여 return
def solution(hp):
    answer = 0
    for ant in [5, 3, 1]:
        d, hp = divmod(hp, ant)
        answer += d
    return answer



# 다른 사람의 풀이 
# hp // 5 : 5로 나눌 수 있는 몫을 구함. 즉, 장군개미 수를 구함
# (hp % 5 // 3) : 5로 나눈 나머지에 3으로 나눈 몫을 구함. 즉, 장군개미를 구하고 남은 나머지 수에서 병정개미의 수를 구함
# ((hp % 5) % 3) : 장군개미와 병정개미를 모두 구하고 남은 나머지. 즉, 일개미의 수
# 모두 더하여 return
def solution(hp):
    return hp // 5 + (hp % 5 // 3) + ((hp % 5) % 3)