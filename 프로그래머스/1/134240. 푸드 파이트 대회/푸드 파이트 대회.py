import math 

def solution(food):
    
    answer = ''
    for (level, amount) in enumerate(food):
        if(level != 0):
            for i in range(0, int(math.floor(amount/2))):
                answer += str(level)
    list_a = list(answer)
    reverse_list = list(reversed(list_a))
    list_a.append('0')
    result_list = list_a + reverse_list
    answer = ''.join(s for s in result_list)
    return answer