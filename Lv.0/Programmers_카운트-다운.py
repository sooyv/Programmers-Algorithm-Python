# 나의 풀이
# for문을 통해서 start부터 end_num까지, -1씩 감소한 리스트를 return
def solution(start, end_num):
    return [i for i in range(start, end_num-1, -1)]