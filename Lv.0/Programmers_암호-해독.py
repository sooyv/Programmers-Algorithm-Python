# 나의 풀이
# for문을 순회하며 code-1부터, cipher의 총길이까지, code만큼 떨어진 문자를 선택
# 문자열의 시작은 0부터이기 때문에 code-1
# answer에 합친 글자를 return
def solution(cipher, code):
    answer = ''
    for i in range(code-1,len(cipher),code):
        answer += cipher[i]
    return answer


# 다른 사람의 풀이
# 슬라이싱 사용 - a[start : end : step]
# code-1부터 끝까지 code만큼 떨어진 문자들을 선택하여 return
def solution(cipher, code):
    return cipher[code-1::code]
