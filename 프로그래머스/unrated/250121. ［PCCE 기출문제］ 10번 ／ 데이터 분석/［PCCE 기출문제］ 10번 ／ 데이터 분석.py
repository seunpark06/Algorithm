##람다식 표현 익혀두기
def solution(data, ext, val_ext, sort_by):
    ext_dict = {"code":0, "date":1, "maximum":2, "remain":3}
    answer = []
    for d in data:
        if(d[ext_dict[ext]] < val_ext):
            answer.append(d)
            
    answer.sort(key = lambda x : x[ext_dict[sort_by]])
    
    return answer