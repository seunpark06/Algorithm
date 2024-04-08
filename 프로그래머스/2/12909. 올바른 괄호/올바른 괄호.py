def solution(s):
    answer = True
    stack = []
    
    for i in s:
        if (i == '('):
            stack.append('(')
        elif i == ')' and stack: #empty list는 false 출력
            stack.pop()
        else:
            return False
    # 스택이 비어있으면 true 반환    
    if not stack:
        return True

    return False