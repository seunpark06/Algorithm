import re

def solution(s):
    answer = True
    if(len(s) == 4 or len(s) == 6): answer = True
    else: answer = False
    
    if(answer):
        return s.isdigit()
    else:
        return False
    
    