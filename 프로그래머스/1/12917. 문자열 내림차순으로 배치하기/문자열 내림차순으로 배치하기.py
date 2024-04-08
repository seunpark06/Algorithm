def solution(s):
    answer = ''
    upperlist = []
    lowerlist = []
    
    for letter in s:
        if(s.isupper()):
            uppderlist.append(letter)
        else:
            lowerlist.append(letter)
            
    upperlist.sort(reverse = True)
    lowerlist.sort(reverse = True)
    
    for i in upperlist:
        answer += i
    
    for i in lowerlist:
        answer += i
    return answer