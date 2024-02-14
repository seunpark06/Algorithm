def solution(s):
    ## 문자열 뒤집기
    reverse_s = ''.join(reversed(s))
    answer = []
    for (index, letter) in enumerate(reverse_s):
        
        value = reverse_s.find(letter, index+1)
       
        if(value > 0):
            answer.append(value - index)
        else:
            answer.append(-1)
    answer.reverse()
    return answer