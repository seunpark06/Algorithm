def solution(number):
    answer = 0
    
    for index in range(0, len(number)-2):
        num1 = number[index]
        for j in range(index+1, len(number)-1):
            num2 = number[j]
            for k in range(j+1, len(number)):
                num3 = number[k]
                if(num1 + num2 + num3 == 0):
                    answer += 1
    return answer