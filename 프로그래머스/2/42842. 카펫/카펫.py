def solution(brown, yellow):
    answer = []
    #카펫의 전체 면적
    s = brown + yellow
    
    #카펫의 가로 길이 탐색
    for width in range(s-1, 0, -1):
        if s % width != 0:
            continue;
        
        #카펫의 세로 길이
        height = s/width
        
        if (height-2) * (width -2) == yellow:
            answer.append(width)
            answer.append(height)
            break
    return answer