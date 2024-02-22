def solution(s):
    answer = 0
    x_count = 0
    o_count = 0
    x = s[0]
    
    for index, element in enumerate(s):
        ## if문 순서 주의  
        if(x_count == o_count):
            answer += 1
            x = element
        if(element == x):
            x_count += 1
        else:
            o_count += 1
        
    return answer