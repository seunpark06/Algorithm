def solution(id_list, report, k):
    answer = []
    # 신고 당한 유저 내역 (to:from)
    to_complain = { i : [] for i in id_list }
    # 신고한 유저의 내역 (from:to)
    from_complain = { i : [] for i in id_list }
    # 정지 당한 유저 아이디
    stop_id = []
    
    for r in report:
        from_p, to_p = r.split(' ')
        #값이 중복되어 들어가는 것 방지
        if from_p not in to_complain[to_p]: 
            to_complain[to_p].append(from_p)
        if to_p not in from_complain[from_p]:
            from_complain[from_p].append(to_p) 
        
    # 신고당한 횟수가 k회 이상이면 아이디 정지
    for user in id_list:
        if(len(to_complain[user])) >= k: stop_id.append(user)
            
    for f in from_complain.values():
        count = 0
        for g in f:
            if(g in stop_id):
                count += 1
        answer.append(count)
                
    return answer