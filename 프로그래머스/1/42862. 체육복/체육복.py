def solution(n, lost, reserve):
    answer = 0
    
    lost.sort()
    reserve.sort()
    
    #중복 제거
    # 체육복을 도난당한 학생이 여벌옷을 가지고 있는 경우
    for l in lost[:]:
        if(l in reserve):
            lost.remove(l)
            reserve.remove(l)

    # 체육복이 2개인 학생을 순환
    for r in reserve:
        #빌려줄 수 있는지 확인
        if(r-1 in lost):
            lost.remove(r-1)
        elif(r+1 in lost):
            lost.remove(r+1)
    
    return n - len(lost)
        
    