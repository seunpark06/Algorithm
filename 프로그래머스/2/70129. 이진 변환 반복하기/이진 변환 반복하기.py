def solution(s):
    answer = []
    bin_num = 0
    num = 0
    new_str = ''
    while len(s) != 1:
        temp = len(s)
        new_str = s.replace('0', '')
        num += (temp - len(new_str)) # 제거된 0의 개수
        s = str(format(len(new_str), 'b')) #2진수로 변환
        bin_num += 1
    
    
    answer = [bin_num, num]
    return answer