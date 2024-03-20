def solution(numbers):
    answer = []
    for index, i in enumerate(numbers):
        for j in numbers[index+1:]:
            answer.append(i+j)
    answer = list(set(answer))
    answer.sort()
    return answer