def solution(answers):
    answer = []
    person = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    
    #정답 개수 카운트
    sum1, sum2, sum3 = 0, 0, 0
    
    for p in range(3):
        if(len(answers) > len(person[p])):
            mok = len(answers) // len(person[p])
            r =len(answers)  %len(person[p])
            person[p] = person[p] * mok + person[p][0:r]
            print(mok, r)
    
    for i in range(len(answers)):
        if(answers[i] == person[0][i]):
            sum1 += 1
        if(answers[i] == person[1][i]):
            sum2 += 1
        if(answers[i] == person[2][i]):
            sum3 += 1
    
    result = max(sum1, sum2, sum3)
    if(result == sum1):
        answer.append(1)
    if(result == sum2):
        answer.append(2)
    if(result == sum3):
        answer.append(3)
    return answer