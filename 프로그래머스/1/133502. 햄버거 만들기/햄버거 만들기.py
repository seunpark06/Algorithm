def solution(ingredient):
    answer = 0
    list_a = []
    ham_list = [1, 2, 3, 1]
    ## 1 2 3 1 빵 야채 고기 빵 => 햄버거 1개
    
    for item in ingredient:
        list_a.append(item)
        if(list_a[-4:] == ham_list):
            answer += 1
            for i in range(4):
                list_a.pop()
        
    return answer