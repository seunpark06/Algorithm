def solution(board, moves):
    ## 터트려져 사라진 인형의 개수
    answer = 0
    ## 게임 화면 가로의 길이
    height = len(board[0])
    ## 인형 바구니
    doll_stack = []
    
    for m in moves:
        i = 0
        while(board[i][m-1] == 0 and i < height -1):
            i += 1
        
        ## 인형이 있는 경우
        if(board[i][m-1] != 0):
            print(i, m, 'm', '인형:', board[i][m-1])
            doll_stack.append(board[i][m-1])
            board[i][m-1] = 0  # 인형을 뽑고 빈칸으로 전환
        
        if(len(doll_stack) > 1 and doll_stack[-1] == doll_stack[-2]):
            doll_stack.pop()
            doll_stack.pop()
            answer += 2
    return answer