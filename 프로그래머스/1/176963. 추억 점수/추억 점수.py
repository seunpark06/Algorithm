def solution(name, yearning, photo):
    my_dic = {}
    for i in range(len(name)):
        key = name[i]
        my_dic[key] = yearning[i]
    
    answer = []
    for pic in photo:
        sum = 0
        for nam in pic:
            if(nam in name):
                sum += my_dic[nam]      
        answer.append(sum)
            
    return answer