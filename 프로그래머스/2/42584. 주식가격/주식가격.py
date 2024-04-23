from collections import deque

def solution(prices):
    answer = []
    # 덱 생성
    q = deque(prices)
     
    while q:
        x = q.popleft()
        cnt = 0 
        
        for i in q:
            cnt += 1
            if x > i:
                break
        answer.append(cnt)
        
    return answer