import math 
  
## 재귀함수로 풀었을때 런타임 에러가나서 반복문으로 바꿔서 다시풀었음
def solution(a, b, n):
    ##answer = cal_bottle(a, b, n)
    answer = 0
    
    ## n과 a가 똑같은 경우도 고려해주어야 한다
    while(n >= a):
        q = math.floor(n/a)
        
        answer += q * b
        n = n - q * a + q * b
    return answer