def solution(n):
    next_num = n + 1
    
    while(str(bin(n)).count('1')  != str(bin(next_num)).count('1')):
        next_num += 1
        
    return next_num