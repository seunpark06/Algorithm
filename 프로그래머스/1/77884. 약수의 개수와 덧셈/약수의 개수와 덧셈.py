import math

def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        count = 0
        # 제곱근이 정수라면 약수의 갯수가 홀수임을 이용한다
        if(math.ceil(math.sqrt(i)) == math.floor(math.sqrt(i))):
            answer -= i
        else: answer += i
            
    return answer