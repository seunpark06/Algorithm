from collections import deque

def solution(s):
    
    answer = 0
    q = deque(s)
    
    for i in range(len(s)):
        temp = q.popleft()
        q.append(temp) # 회전
        
        if check_correct(q):
            answer += 1
    return answer

def check_correct(q):
    s_pairs = { ')':'(', '}':'{', ']':'[' }
    # 올바른 괄호 문자열인지 확인
    stack = []
    for j in q:
        if len(stack) == 0: stack.append(j) #마지막에 stack 길이로 판별하기 위함
        else:   
            if j in ')}]':
                if stack and s_pairs[j] == stack[-1]:
                    stack.pop()
                else: #올바르지 않은 괄호의 경우
                    break;
            else: # 열린 괄호인 경우
                stack.append(j)
    return len(stack) == 0
