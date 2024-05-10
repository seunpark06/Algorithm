def solution(skill, skill_trees):
    answer = len(skill_trees)
    
    for st in skill_trees:
        s_temp = ""
        st_list = list(st)
        for s in st_list:
            if s in skill: 
                s_temp += s

        for idx, i in enumerate(s_temp): #선행스킬이 필요한 스킬의 인덱스 비교
            if skill.index(i) != idx:
                answer -= 1
                break
        
    return answer