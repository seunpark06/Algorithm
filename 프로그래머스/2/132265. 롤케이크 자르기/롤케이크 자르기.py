def solution(topping):
    answer = 0
    
    bro1 = {} #형의 롤케잌
    bro2 = {} #동생의 롤케잌
    
    for t in topping:
        if t in bro1: #이미 있는 토핑이라면
            bro1[t] += 1
        else:
            bro1[t] = 1
        
    for t in topping:
        if len(bro1) == len(bro2): #공평한 분배
            answer += 1
        
        #동생 케이크에 없는 토핑이라면 추가해준다
        if t not in bro2:
            bro2[t] = 1
            
        bro1[t] -= 1
        if bro1[t] == 0:
            del bro1[t]
        
    return answer