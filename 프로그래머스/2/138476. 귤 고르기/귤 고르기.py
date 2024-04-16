def solution(k, tangerine):
    answer = 0
    t_max = max(tangerine)
    # 귤이 크기별로 몇 개 있는지 저장
    t_dict = { i:0 for i in range(1, t_max+1) }
    for t in tangerine:
        t_dict[t] += 1
    temp = sorted(t_dict.values(), reverse=True)

    for num in temp:
        k -= num
        answer += 1
        if(k <= 0):
            return answer
        
