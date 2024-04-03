def solution(survey, choices):
    answer = ''
    result = ''
    person_dict = {i:'' for i in range(1, 5)}
    category = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    for c, s in zip(choices, survey):
                
        if(c - 4) > 0: # 약간 동의(5), 동의(6), 매우 동의(7)
            answer += s[1:] * (c - 4)
        elif(c - 4) < 0: # 매우 비동의, 비동의, 약간 비동의
            answer += s[0:1] * abs(c - 4)
    for cg in category:
        if(answer.count(cg[0]) > answer.count(cg[1])):
            result += cg[0]
        elif(answer.count(cg[0]) < answer.count(cg[1])):
            result += cg[1]
        else: # 선택 점수가 같은 경우
            result += min(cg[0], cg[1]) #알파벳 순으로 낮은 것을 선택한다
    return result