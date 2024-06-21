from collections import deque

def solution(priorities, location):
    answer = 0 #실행되는 프로세스의 수(몇 번째로 실행되는지)
    q = deque(priorities)        
    
    while q:
        max_p = max(q) #우선순위 가장 큰 값
        cur = q.popleft() #큐에서 하나를 꺼낸다
        location -= 1
        if cur != max_p: #대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면
            q.append(cur) #다시 큐에 넣는다
            if location  < 0: #꺼낸 프로세스가 목표 프로세스인경우
                location = len(q) -1 #큐 가장 뒤로 넣는다
        else: # 프로세스 실행
            answer += 1
            if location < 0:
                break;
    return answer