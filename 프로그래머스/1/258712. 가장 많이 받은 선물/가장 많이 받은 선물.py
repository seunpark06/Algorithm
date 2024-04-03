def solution(friends, gifts):
    answer = 0
    cols = len(friends)
    rows = len(friends)
    record_gift = [[0 for i in range(rows)] for j in range(cols)]
    
    ## 두 사람이 선물 주고받은 기록들을 2차원 배열에 저장한다
    for record in gifts:
        temp = record.split(' ')
        ## 선물을 준 사람 (행)
        i = friends.index(temp[0])
        ## 선물을 받은 사람(열)
        j = friends.index(temp[1])
        record_gift[i][j] += 1
        
        count = 0
        result = 0
        sumA,sumB = 0,0
        
        ## 선물 지수 계산
        gift_score = []
        to_me = []
        from_me = []
        
        # 준 선물
        for r in range(rows):
            temp = 0
            for c in range(cols):
                temp += record_gift[r][c]
            from_me.append(temp)
        
        # 받은 선물
        for c in range(cols):
            temp = 0
            for r in range(rows):
                temp += record_gift[r][c]
            to_me.append(temp)
            
        # 선물 지수 계산
        for i in range(rows):
            gift_score.append(from_me[i] - to_me[i])
        
        ## 각 사람이 받는 선물의 수
        for k in range(rows):
            count = 0
            for l in range(cols):
                ## 선물 주고받은 기록 비교
                if(record_gift[k][l] > record_gift[l][k]):
                    count += 1
                ## 선물을 주고받은 수가 같다면
                elif(record_gift[k][l] == record_gift[l][k]):
                    ## 선물 지수 비교
                    if(gift_score[k] > gift_score[l]):
                        count += 1
                        
            result = max(count, result)
        
            
    return result