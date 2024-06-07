def solution(storey):
    answer = 0
    stack = []
    temp = str(storey)
    
    for i in range(len(temp)):
         stack.append(int(temp[i:i+1]))
    
    
    while stack:
        std = stack.pop()
        if std > 5:
            answer += 10 - std
            if stack:
                stack[-1] += 1
            else:
                answer += 1
        elif std < 5:
            answer += std
        else: #자릿수가 5인 경우
            if stack and stack[-1] >= 5:
                answer += 10 - std
                stack[-1] += 1
            else:
                answer += std
            
            
    
    return answer