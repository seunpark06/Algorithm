def solution(array, commands):
    answer = []
    for c in commands:
        result = array[c[0]-1:c[1]]
        print(result)
        result.sort()
    
        answer.append(result[c[2]-1]) 
    return answer