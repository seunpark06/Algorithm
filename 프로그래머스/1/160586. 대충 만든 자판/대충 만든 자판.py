def solution(keymap, targets):
    answer = []
    
    ## 모든 key의 최단거리를 가지는 key_dict 생성
    key_dict = {}
    for key in keymap:
        for k in key:
            if(k in key_dict):
                key_dict[k] = min(key.index(k) + 1, key_dict[k])
            else:
                key_dict[k] = key.index(k) + 1
    
    
    for target in targets:
        count = 0
        for t in target:
            if(t in key_dict):
                count += key_dict[t]
            else:
                count = -1
                break;
        answer.append(count)
    
    return answer