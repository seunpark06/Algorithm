def solution(lottos, win_nums):
    hit = 0
    hit_nums = []
    answer = []
    missing = 0
    for l in lottos:
        if(l in win_nums):
            hit += 1
            hit_nums.append(l)
        ## 지워진 숫자의 수
        if(l == 0):
            missing += 1
    
    min_ranking, max_ranking = 0,0
    ## 적중한 번호 개수에 따라 분기처리
    if(hit == 6):
        min_ranking, max_ranking = 1, 1
    elif(hit == 0 or hit == 1):
        min_ranking = 6
        if(hit + missing == 6):
            max_ranking = 1
        elif(hit + missing == 0 or hit + missing == 1):
            max_ranking = 6
        else:
            max_ranking = 7-(hit + missing)
    else:
        min_ranking = 7 - hit
        max_ranking = min_ranking - missing
    
    answer.append(max_ranking)
    answer.append(min_ranking)
    return answer