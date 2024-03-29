def solution(babbling):
    answer = 0
    says = ["aya", "ye", "woo", "ma" ]
    
    for b in babbling:
        result = 0
        for s in says:
            if s*2 not in b:
                b = b.replace(s, ' ')
        if(b.isspace()):
            answer += 1
    
    return answer