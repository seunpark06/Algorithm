def solution(s):
    answer = ''
    n_list = []
    for num in s.split(" "):
        n_list.append(int(num))
        
    answer += str(min(n_list))
    answer += " "
    answer += str(max(n_list))
    return answer