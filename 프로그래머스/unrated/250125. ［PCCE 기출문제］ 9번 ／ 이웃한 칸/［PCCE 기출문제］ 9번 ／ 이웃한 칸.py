##참고: 문제에서 의사코드가 주어져서 난이도가 매우 쉬웠음
def solution(board, h, w):
    n = len(board)
    count = 0
    
    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]
    
    for i in range(0, 4, 1):
        h_check = h + dh[i]
        w_check = w + dw[i]        
        if((0 <= h_check and h_check < n) and (0 <= w_check and w_check < n)):
            if(board[h][w] == board[h_check][w_check]):
                print('값', h, w)
                count += 1
    answer = count
    return answer