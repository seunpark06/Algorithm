def solution(k, score):
    answer = []
    winner = []
    for (index, sc) in enumerate(score):
        # 1일 ~ k일
        if(index < k):
            winner.append(sc)
            winner_s = sorted(winner)
            answer.append(winner_s[0])
            
        ## k일이 지난경우
        else:
           ## winner_set = set(winner)
            ##winner = list(winner_set)            
            winner.sort(reverse = True)
            
            if(sc > winner[-1]):
                winner[-1] = sc
            
            winner.sort(reverse = True)
            answer.append(winner[-1])
                        
    return answer