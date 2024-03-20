def solution(n):
    answer = ''
    mok = 0
    re = 0
    while n> 0:        
        re = n % 3
        n = n // 3
        answer += str(re) 
    
    return int(answer, 3)

# int(x, base) : base 진법으로 구성된 str 형식의 수를 10진법으로 변환해 줌