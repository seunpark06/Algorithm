from collections import deque
def solution(progresses, speeds):
    answer = []
    p_queue = deque(progresses)
    s_queue = deque(speeds)
    
    while len(p_queue) > 0: #큐가 비어있지 않으면 
        
        #매일 작업 진도율 반영
        for i in range(len(p_queue)):
            p_queue[i] += s_queue[i]
            
        cnt = 0
        while p_queue and p_queue[0] >= 100: #순위가 높은 작업이 끝나면
            print(p_queue)
            p_queue.popleft()
            s_queue.popleft()
            cnt += 1
        if cnt > 0: answer.append(cnt)
        
        
    return answer