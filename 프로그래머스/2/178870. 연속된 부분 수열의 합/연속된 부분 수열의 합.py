def solution(sequence, k):
    # l, r 값을 정의해서
    # l 부터 r까지 더한 값이 k보다 큰 경우 l 증가
    # l 부터 r까지 더한 값이 k보다 작은 경우 r 증가
    
    l, r = 0, 0
    total = sequence[0]
    answer = [0, len(sequence)]
    
    while True:
        if total < k:
            r += 1
            if r == len(sequence): #끝까지 순회가 끝나면 반환
                break
            total += sequence[r]
            
        else: #같거나 큰 경우
            if total == k:
                if answer[1] - answer[0] >  r - l:
                    answer = [l, r]
            total -= sequence[l]
            l += 1
            
    
    return answer