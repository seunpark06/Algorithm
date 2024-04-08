def solution(s):
    answer = 0
    if(s[0:1] != '-'):
        answer = int(s[:])
    else:
        answer = 0 - int(s[1:])
    return answer