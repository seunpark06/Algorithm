def solution(elements):
    answer = 0
    new_list = elements * 2
    sum_list = []
    # print(new_list)
    
    sum_list.append(sum(elements))
    for i in range(len(elements)):
        for j in range(1, len(elements)):
            sum_list.append(sum(new_list[i:i+j]))
        
    
    sum_list = list(set(sum_list))
    answer = len(sum_list)
    return answer