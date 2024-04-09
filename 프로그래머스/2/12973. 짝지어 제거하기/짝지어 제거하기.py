def solution(s):
    answer = -1
    stack = []
    
    s = list(s)
    # s.reverse()    
    for i in s:        
        # 스택이 비어있지 않고, top이 넣으려는 문자와 같으면
        if(stack and stack[-1] == i):
            stack.pop()
        else:
            stack.append(i)
    
    if stack: return 0
    else: return 1
