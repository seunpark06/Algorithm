def solution(s):
    answer = ''
    temp = s.split(" ")
    for i, t in enumerate(temp):
        t = t[0:1].upper() + t[1:].lower()
        answer += t
        if(i < len(temp) -1):
            answer += " "
    return answer