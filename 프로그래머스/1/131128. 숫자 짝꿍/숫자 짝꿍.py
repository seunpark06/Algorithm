def solution(X, Y):
    answer = ""
    
    ## 문자열 X, Y에서 등장하는 숫자들을 딕셔너리 형태로 저장
    ## 숫자: 포함개수
    numx = {}
    numy = {}
    
    for i in range(10):
        numx[str(i)] = 0
        numy[str(i)] = 0
    
    for x in X:
        numx[x] += 1
    
    for y in Y:
        numy[y] += 1
        
    print(numx)
    print(numy)
    
    ## 9부터 0까지 카운트
    for i in range(9, -1, -1):
        i = str(i)
        iternum = min(numx[i], numy[i])   
        
        if answer == '' and i == '0' and iternum != 0:
            return "0"
        
        answer = ''.join([answer, iternum*i])
    if answer == "":
        return "-1"   
    else:
        return answer