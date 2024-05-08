# 다른 사람의 풀이 1
# 첫번째 풀이 - 테스트 코드 13, 14 실패
# 제한 사항 : price는 10원 단위(1의 자리가 0)
# 소수점 이하를 버린 정수를 return 합니다.
# 반례 : 입력값 - 100030, 기댓값 - 95028 일때, 결괏값 95028.5로 테스트 코드 싫패
def solution(price):
    if price >= 500000:
        return price - price * 0.2
    elif price >= 300000:
        return price - price * 0.1
    elif price >= 100000:
        return price - price * 0.05
    else:
        return price
    
    
# 두번째 풀이
# int(price) 로 정수부만을 return 하도록 수정
def solution(price):
    if price >= 500000:
        price = price - price * 0.2
    elif price >= 300000:
        price = price - price * 0.1
    elif price >= 100000:
        price = price - price * 0.05
    return int(price)



# 다른 사람의 풀이 1
    # for in 뒤에 딕셔너리를 지정하고 items을 사용하여 키와 값을 모두 확인
    # for 키, 값 in 딕셔너리.items():
    #     반복할 코드
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
        
        
# 다른 사람의 풀이 2
def solution(price):
    return (100 - len([1 for k in [100000, 300000, 500000, 500000] if k<=price])*5) * price // 100