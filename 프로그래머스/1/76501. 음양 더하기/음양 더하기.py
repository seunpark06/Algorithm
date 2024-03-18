def solution(absolutes, signs):
    answer = 0
    for index, num in enumerate(absolutes):
        if signs[index]:
            answer = answer + num
        else:
            answer = answer -num
    return answer