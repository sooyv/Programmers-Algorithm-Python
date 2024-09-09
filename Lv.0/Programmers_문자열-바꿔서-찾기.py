# 나의 풀이 1
# for문으로 myString 문자열을 순회하며 i를 확인한다.
# 삼항연산자를 통해 i가 "A"라면 str에 "B"를 추가하고, 
# "A"가 아니라면(="B"라면) "A"를 추가하여 "A"와 "B"를 변환한다.
# 변환된 문자열 str에 pat이 있는지 확인하여 true, false를 int 정수형으로 변환해 return한다.
def solution(myString, pat):
    str = ''
    for i in myString:
        str += "B" if i == "A" else "A"
        
    return int(pat in str)


# 나의 풀이 2
# 리스트 컴프리헨션을 이용하여 myString의 각 문자 i를 순회하고
# 삼항연산자를 이용하여 "A"는 "B"로, "B"는 "A"로 변환한다.
# ''.join([...])을 사용하여 변환된 문자들을 하나의 문자열로 결합한다.
# pat in 으로 문자열에 pat이 포함되는지 확인하고 true, false를 int 정수형으로 변환해 return한다.
def solution(myString, pat):
    return int(pat in ''.join(["B" if i == "A" else "A" for i in myString]))



# 다른 사람의 풀이 1
# "C" 라는 임시 문자를 통한 풀이

# myString의 모든 "A"를 임시 문자 "C"로 변환하고, "B"를 "A"로 변환한다. 
# 다시 임시 문자 "C"를 "B"로 변환하여 원래의 "A"를 "B"로, 원래의 "B"를 "A"로 변환한다.
# 변환된 문자열에서 pat이 포함되어 있는지를 확인하여 포함 여부를 int 정수형으로 반환한다.
def solution(myString, pat):
    return int(pat in myString.replace('A', 'C').replace('B', 'A').replace('C', 'B'))


# 다른 사람의 풀이 2
# myString이 아닌 pat을 변환한 풀이

## 풀이 방법은 나의 풀이 2번과 동일 ##
def solution(myString, pat):
    return int(''.join(['A' if i == 'B' else 'B' for i in pat]) in myString)

