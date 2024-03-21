def solution(today, terms, privacies):    
    answer = []
    terms_dict = {}
    
    ## 약관과 유효기간을 딕셔너리 형태로 저장
    for t in terms:
        temp = t.split(" ") #공백으로 분리
        terms_dict[temp[0]] = int(temp[1])
    
    ## 보관 가능한 날짜 계산 (모든 달이 28일까지 있다고 가정)
    for index, t in enumerate(privacies):
        p_arr = t.split(" ")
        date = p_arr[0].replace(".", "")
        term = p_arr[1]
        start_year = int(date[0:4])
        start_month = int(date[4:6])
        start_day = int(date[6:])
        
        end_month = start_month + terms_dict[term]
        end_day = start_day - 1
        end_year = start_year
        
        if(end_day == 0):
            end_day = 28
            end_month -= 1
        while(end_month > 12):
            end_month -= 12
            end_year += 1
        
        end = str(end_year) + str(end_month).zfill(2) + str(end_day).zfill(2)
        ## 약관 날짜와 비교
        if(end < today.replace(".", "")):
            print(end)
            answer.append(index+1)
    
    return answer