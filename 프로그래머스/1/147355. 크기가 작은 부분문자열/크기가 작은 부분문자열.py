def solution(t, p):
    answer = 0
    range_num = len(t) - len(p) + 1
    for i in range(range_num):
        t_num = t[i: i+len(p)]
        
        if(int(t_num) <= int(p)):
            answer += 1
    return answer