## 이전에 칠한 구역보다 m-1 이상 큰 구역이 나올때 1씩 count 증가
def solution(n, m, section):
    answer = 1
    start = section[0]
    for num in section:
        if(start + m - 1 < num ):
            answer += 1
            start = num
    
    return answer