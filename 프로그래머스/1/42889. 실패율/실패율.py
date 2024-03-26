from collections import Counter

def solution(N, stages):
    answer = []
    counter1 = Counter(stages)
    
    fault_dict = {i:0 for i in range(1,N+1)}
    # 전체 사용자 수
    dodal = len(stages)
    for s in range(0, N):
        if(dodal == 0):
            fault_dict[s+1] = 0
        else:
            # i+1 번째 스테이지의 실패 계산        
            fault_dict[s+1] = float((counter1[s+1])/dodal)
            dodal -= counter1[s+1] # 다음 스테이지에 도달한 사람 수
    
    sort_dict = dict(sorted(fault_dict.items(), key=lambda x: x[1], reverse= True))
    answer = list(sort_dict.keys())
    return answer

    