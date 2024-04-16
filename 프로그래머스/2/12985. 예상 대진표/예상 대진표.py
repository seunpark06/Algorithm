import math

def solution(n,a,b):
    answer = 1
    # 이겼을 경우 갖게 되는 번호를 구한다
    a_next = math.ceil(a/2) 
    b_next = math.ceil(b/2)
    while a_next != b_next:
        a_next = math.ceil(a_next/2)        
        b_next = math.ceil(b_next/2)        
        answer += 1

    return answer