def solution(n, words):
    answer = [0, 0]
    temp = words[0]
    for i in range(len(words) -1):
        next_word = words[i + 1]
        if temp[-1] != next_word[0] or next_word in words[:i]: #끝말잇기 규칙 위배
            answer[0] = (i + 1) % n + 1
            answer[1] = (i + 1) // n + 1
            
            return answer            
            
        else: # i+1번째로 외친 사람 탈락
            temp = words[i + 1]

    return answer