from collections import deque

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(maps):
    q = deque()
    q.append((0, 0))
    maps[0][0] = 1 
    n = len(maps) #세로
    m = len(maps[0]) #가로 길이
    
    while q: #큐가 비어있을 때까지 순환
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if maps[nx][ny] == 1: #벽이 아니면
                q.append((nx, ny))
                # x, y = nx, ny
                maps[nx][ny] = maps[x][y] + 1
                
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]

def solution(maps):
    answer= dfs(maps)
    # print(maps)
    return answer