def solution(k, m, score):
    answer = 0
    
    score.sort(reverse=True)

    
    for i in range(0, len(score)-1, m):
        answer += min(score[i:i+m])*m
        if(i+m > len(score)):
            return answer - min(score[i:i+m])*m
    
    return answer