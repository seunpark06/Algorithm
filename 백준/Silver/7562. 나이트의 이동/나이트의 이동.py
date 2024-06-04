from collections import deque

#나이트가 움직일 수 있는 범위
dx = [2, 1, -1, -2, 1, 2, -1, -2]
dy = [1, 2, -2, -1, -2, -1, 2, 1]

def bfs(x, y, t1, t2):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        if (x, y) == (t1, t2): #목표 지점에 도달하면
            print(graph[t1][t2] -1 ) #시작 지점에서 1을 넣어줬기때문에 도착지에서 -1 해준다
            return True

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= k or ny < 0  or ny >= k: # 체스판 범위를 벗어나는 경우
                continue

            # 이동한 거리를 저장한다
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny)) #큐에 이동할 위치를 추가해준다

n = int(input()) # 테스트케이스의 수

for _ in range(n):
    k = int(input())  # 체스판의 한 변의 길이
    graph = [(k)*[0] for _ in range(k)]

    s1, s2 = map(int, input().split()) #시작 위치
    graph[s1][s2] = 1
    t1, t2 = map(int, input().split()) #목표 위치

    bfs(s1, s2, t1, t2)

